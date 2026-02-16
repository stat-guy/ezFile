#!/usr/bin/env python3
"""
EZFile Hook: Validate Output Files
Type: PostToolUse (Write)

Scans files written to the returns/ directory for:
1. Full SSN patterns (must be masked to XXX-XX-NNNN)
2. Basic tax math invariants

Outputs warnings to stderr if issues are found.
"""

import json
import sys
import re
import os


# SSN pattern: exactly 3 digits, dash, 2 digits, dash, 4 digits
# We want to BLOCK full SSNs but ALLOW masked ones (XXX-XX-NNNN)
FULL_SSN_PATTERN = re.compile(r'\b\d{3}-\d{2}-\d{4}\b')
MASKED_SSN_PATTERN = re.compile(r'XXX-XX-\d{4}')

# SSN without dashes (9 consecutive digits that could be an SSN)
BARE_SSN_PATTERN = re.compile(r'\b\d{9}\b')


def check_for_ssn(content: str) -> list[str]:
    """Check for unmasked SSN patterns in content."""
    warnings = []

    # Find all SSN-like patterns
    ssn_matches = FULL_SSN_PATTERN.findall(content)

    for match in ssn_matches:
        # Check if this is a masked SSN (XXX-XX-NNNN) -- those are OK
        # Since the regex only matches digits, any match here is a FULL SSN
        warnings.append(
            f"FULL SSN DETECTED: '{match}' -- "
            "Must be masked to XXX-XX-NNNN format"
        )

    # Also check for 9 consecutive digits that might be unformatted SSNs
    # But exclude common false positives (ZIP+4, phone numbers, EINs, etc.)
    bare_matches = BARE_SSN_PATTERN.findall(content)
    for match in bare_matches:
        # Skip if it looks like a ZIP+4 (5+4 digits)
        if match[:5].isdigit() and match[5:].isdigit():
            # Could be a ZIP+4, but also could be an SSN
            warnings.append(
                f"WARNING: 9-digit number '{match}' detected -- "
                "verify this is not an unformatted SSN"
            )

    return warnings


def check_tax_math(data: dict) -> list[str]:
    """Verify basic tax math invariants in JSON data."""
    warnings = []

    # Check if this looks like a tax return JSON
    if not isinstance(data, dict):
        return warnings

    # Invariant 1: taxable_income = AGI - deductions (if all present)
    agi = data.get("agi") or data.get("adjusted_gross_income") or data.get("line_11")
    deductions = data.get("total_deductions") or data.get("line_14")
    taxable = data.get("taxable_income") or data.get("line_15")

    if agi is not None and deductions is not None and taxable is not None:
        expected = max(float(agi) - float(deductions), 0)
        actual = float(taxable)
        if abs(expected - actual) > 0.01:
            warnings.append(
                f"MATH ERROR: AGI ({agi}) - deductions ({deductions}) = "
                f"{expected}, but taxable income = {actual}"
            )

    # Invariant 2: refund = payments - total_tax (if refund exists)
    total_tax = data.get("total_tax") or data.get("line_24")
    payments = data.get("total_payments") or data.get("line_33")
    refund = data.get("refund") or data.get("line_34")
    owed = data.get("amount_owed") or data.get("line_37")

    if total_tax is not None and payments is not None:
        total_tax = float(total_tax)
        payments = float(payments)

        if refund is not None:
            expected_refund = payments - total_tax
            actual_refund = float(refund)
            if abs(expected_refund - actual_refund) > 0.01:
                warnings.append(
                    f"MATH ERROR: payments ({payments}) - total_tax ({total_tax}) = "
                    f"{expected_refund}, but refund = {actual_refund}"
                )

        if owed is not None:
            expected_owed = total_tax - payments
            actual_owed = float(owed)
            if abs(expected_owed - actual_owed) > 0.01:
                warnings.append(
                    f"MATH ERROR: total_tax ({total_tax}) - payments ({payments}) = "
                    f"{expected_owed}, but amount_owed = {actual_owed}"
                )

    # Invariant 3: tax should be non-negative
    tax = data.get("tax") or data.get("line_16")
    if tax is not None and float(tax) < 0:
        warnings.append(f"MATH ERROR: Tax (Line 16) is negative: {tax}")

    # Invariant 4: taxable income should be non-negative
    if taxable is not None and float(taxable) < 0:
        warnings.append(f"MATH ERROR: Taxable income is negative: {taxable}")

    return warnings


def main():
    try:
        input_data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    tool_name = input_data.get("tool_name", "")

    # Only check Write and Edit tools
    if tool_name not in ("Write", "Edit"):
        sys.exit(0)

    tool_input = input_data.get("tool_input", {})
    file_path = tool_input.get("file_path", "")

    if not file_path:
        sys.exit(0)

    # Only validate files in the returns/ directory
    if "returns/" not in file_path and "returns\\" not in file_path:
        sys.exit(0)

    # Read the file that was just written
    try:
        with open(file_path, "r") as f:
            content = f.read()
    except (FileNotFoundError, PermissionError, OSError):
        # File might not exist yet or be inaccessible
        sys.exit(0)

    all_warnings = []

    # Check for SSN patterns
    ssn_warnings = check_for_ssn(content)
    all_warnings.extend(ssn_warnings)

    # Check tax math if it's a JSON file
    if file_path.endswith(".json"):
        try:
            data = json.loads(content)
            math_warnings = check_tax_math(data)
            all_warnings.extend(math_warnings)
        except json.JSONDecodeError:
            pass  # Not valid JSON, skip math check

    # Output warnings
    if all_warnings:
        for warning in all_warnings:
            print(f"EZFile Validation: {warning}", file=sys.stderr)

        # If SSN was found, this is critical -- exit with error
        if any("FULL SSN DETECTED" in w for w in all_warnings):
            print(
                "\nCRITICAL: Full SSN found in output file. "
                "The file must be corrected to mask SSN as XXX-XX-NNNN.",
                file=sys.stderr
            )
            sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
