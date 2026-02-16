#!/usr/bin/env python3
"""
EZFile Hook: Block PII in Web Searches
Type: PreToolUse (WebSearch, WebFetch)

Prevents SSNs, EINs, and other PII patterns from appearing
in web search queries or URL fetches.
"""

import json
import sys
import re


# PII patterns to block
PII_PATTERNS = [
    # SSN: 3 digits, dash, 2 digits, dash, 4 digits
    (r'\b\d{3}-\d{2}-\d{4}\b', "Social Security Number"),
    # SSN without dashes
    (r'\b\d{9}\b', "possible SSN (9 consecutive digits)"),
    # EIN: 2 digits, dash, 7 digits
    (r'\b\d{2}-\d{7}\b', "Employer Identification Number"),
    # Common SSN-like references
    (r'\bSSN\b', "SSN reference"),
    (r'\bsocial\s+security\s+number\b', "Social Security Number reference"),
    # Bank account numbers (8-17 digits)
    (r'\b\d{8,17}\b', "possible account number"),
    # Full names combined with tax-related terms
    # (This is intentionally broad to catch accidental PII leaks)
]


def main():
    try:
        input_data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    tool_name = input_data.get("tool_name", "")

    # Only check WebSearch and WebFetch
    if tool_name not in ("WebSearch", "WebFetch"):
        sys.exit(0)

    tool_input = input_data.get("tool_input", {})

    # Get the search query or URL
    text_to_check = ""
    if tool_name == "WebSearch":
        text_to_check = tool_input.get("query", "")
    elif tool_name == "WebFetch":
        text_to_check = tool_input.get("url", "") + " " + tool_input.get("prompt", "")

    if not text_to_check:
        sys.exit(0)

    # Check for PII patterns
    for pattern, description in PII_PATTERNS:
        match = re.search(pattern, text_to_check, re.IGNORECASE)
        if match:
            result = {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": (
                        f"EZFile: Blocked web request containing {description}. "
                        "Tax-related personal information must never be sent over the network. "
                        f"Detected: '{match.group()}'"
                    )
                }
            }
            print(json.dumps(result))
            sys.exit(0)

    # No PII detected, allow
    sys.exit(0)


if __name__ == "__main__":
    main()
