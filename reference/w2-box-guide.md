# W-2 Box-by-Box Guide

This reference explains every box on Form W-2 and how EZFile uses it.

## Identity Fields

### Box a: Employee's Social Security Number
- **What it is:** Your SSN
- **EZFile handling:** NEVER stored in full. Only last 4 digits extracted (XXX-XX-NNNN)
- **Form 1040:** Entered at top of form

### Box b: Employer Identification Number (EIN)
- **What it is:** Your employer's tax ID
- **EZFile handling:** Stored for reference; not sensitive in the same way as SSN
- **Form 1040:** Not entered directly

### Box c: Employer's Name, Address, and ZIP
- **What it is:** Your employer's official information
- **EZFile handling:** Displayed for verification
- **Form 1040:** Not entered directly

### Box d: Control Number
- **What it is:** Employer's internal tracking number
- **EZFile handling:** Ignored (not needed for filing)

### Box e: Employee's Name
- **What it is:** Your legal name as your employer has it
- **EZFile handling:** Used for display and verification
- **Form 1040:** Must match name on form

### Box f: Employee's Address
- **What it is:** Your address as your employer has it
- **EZFile handling:** Displayed for verification
- **Form 1040:** Not entered directly (you enter current address)

## Core Income & Withholding Fields

### Box 1: Wages, Tips, Other Compensation
- **What it is:** Your total taxable federal wages for the year
- **How it's calculated:** Base salary MINUS pre-tax deductions (retirement, health insurance, HSA, FSA, transit)
- **Why it differs from your salary:** Pre-tax benefits reduce this number. Example: $51,333 salary - $4,107 retirement - $1,500 HSA - other benefits = $44,629
- **Form 1040:** Goes on **Line 1a**
- **EZFile critical:** This is THE number that drives the entire return

### Box 2: Federal Income Tax Withheld
- **What it is:** How much federal tax your employer already sent to the IRS on your behalf
- **How it's determined:** Based on your W-4 elections (filing status, allowances/adjustments)
- **Form 1040:** Goes on **Line 25a**
- **EZFile critical:** This is compared to your actual tax to determine refund or amount owed

### Box 3: Social Security Wages
- **What it is:** Wages subject to Social Security tax
- **How it differs from Box 1:** Does NOT exclude most pre-tax deductions (retirement contributions are still included). Capped at $176,100 for 2025.
- **Form 1040:** Not entered (verification only)
- **EZFile use:** Validation -- Box 4 should equal Box 3 x 6.2%

### Box 4: Social Security Tax Withheld
- **What it is:** Employee's share of Social Security tax (6.2% of Box 3)
- **Maximum for 2025:** $10,918.20 ($176,100 x 6.2%)
- **Form 1040:** Not entered (verification only)
- **EZFile use:** Validation check: Box 4 / Box 3 should ≈ 0.062

### Box 5: Medicare Wages and Tips
- **What it is:** Wages subject to Medicare tax
- **How it differs from Box 3:** No wage cap (all wages are subject to Medicare)
- **Usually equals:** Box 3 (unless wages exceed SS cap of $176,100)
- **Form 1040:** Not entered (verification only)
- **EZFile use:** Validation -- Box 6 should equal Box 5 x 1.45%

### Box 6: Medicare Tax Withheld
- **What it is:** Employee's share of Medicare tax (1.45% of Box 5)
- **Additional Medicare:** If Box 5 > $200,000, extra 0.9% on amount over $200K
- **Form 1040:** Not entered (verification only)
- **EZFile use:** Validation check: Box 6 / Box 5 should ≈ 0.0145

## Special Situations (Boxes 7-11)

### Box 7: Social Security Tips
- **What it is:** Tips reported to employer that are subject to Social Security tax
- **EZFile handling:** Relevant for Schedule 1-A tip deduction
- **Note:** Tips are already included in Box 1

### Box 8: Allocated Tips
- **What it is:** Tips allocated by employer (for large food/beverage establishments)
- **EZFile handling:** NOT included in Box 1 -- may need to be added as income
- **Note:** Rare for this plugin's target user

### Box 9: (Blank / Verification Code)
- **EZFile handling:** Ignored

### Box 10: Dependent Care Benefits
- **What it is:** Employer-provided dependent care assistance (FSA)
- **EZFile handling:** N/A for this plugin (no dependents)
- **Note:** If present, it's informational only for single filers with no dependents

### Box 11: Nonqualified Plans
- **What it is:** Distributions from nonqualified deferred compensation plans
- **EZFile handling:** Already included in Box 1; informational only

## Box 12: Coded Entries (12a through 12d)

Each entry has a letter code and dollar amount. Common codes:

| Code | Description | EZFile Impact |
|---|---|---|
| D | 401(k) elective deferrals | Already excluded from Box 1. Do NOT subtract again. Used for Saver's Credit check. |
| E | 403(b) contributions | Same as Code D. Common for teachers, university employees. |
| G | 457(b) contributions | Same as Code D. Common for government employees. |
| W | HSA employer contributions | Already excluded from Box 1. Informational. |
| AA | Roth 401(k) contributions | NOT excluded from Box 1 (after-tax). Shown for info. |
| BB | Roth 403(b) contributions | Same as AA. |
| DD | Health insurance cost | Informational only. NOT a deduction. |
| C | Group-term life insurance >$50K | Already included in Box 1. Informational. |

### Saver's Credit Relevance
Codes D, E, G, AA, BB represent retirement contributions eligible for the Saver's Credit (Form 8880). EZFile checks these amounts against AGI thresholds.

## Box 13: Checkboxes

### Statutory Employee
- **EZFile handling:** Out of scope. If checked, refer to CPA.

### Retirement Plan
- **What it means:** You participated in an employer retirement plan
- **EZFile impact:** Affects traditional IRA deduction eligibility (not relevant for this plugin's scope, but noted for completeness)

### Third-Party Sick Pay
- **EZFile handling:** Informational only

## Box 14: Other

Employer-specific codes. Common entries:
- State disability insurance (SDI)
- Union dues
- Uniform allowance
- Educational assistance
- Local Service Tax (LST)
- Various fringe benefits

**EZFile handling:** Usually informational. Some states use Box 14 data. Display to user but do not use in federal calculation unless specifically recognized.

## State & Local Fields (Boxes 15-20)

### Box 15: State / Employer's State ID
- **What it is:** Two-letter state code and employer's state tax ID
- **EZFile use:** Determines which state return is needed

### Box 16: State Wages, Tips, Etc.
- **What it is:** Wages subject to state income tax
- **May differ from Box 1:** States have different pre-tax deduction rules
- **EZFile use:** Base for state tax calculation

### Box 17: State Income Tax
- **What it is:** State tax already withheld by employer
- **EZFile use:** Compared to state tax liability for state refund/owed calculation

### Box 18: Local Wages, Tips, Etc.
- **What it is:** Wages subject to local income tax
- **EZFile use:** Base for local tax calculation (if applicable)

### Box 19: Local Income Tax
- **What it is:** Local tax already withheld
- **EZFile use:** Compared to local tax liability

### Box 20: Locality Name
- **What it is:** Name or code of the local taxing jurisdiction
- **EZFile use:** Identifies which local return may be needed

## Validation Rules

After extraction, verify these relationships:

```
1. Box 4 ≈ Box 3 × 0.062    (within $1 rounding tolerance)
2. Box 6 ≈ Box 5 × 0.0145   (within $1 rounding tolerance)
3. Box 1 <= Box 3            (usually; Box 1 can exceed Box 3 if employee has
                               pre-tax deductions that only reduce federal wages)
4. Box 3 <= $176,100         (2025 Social Security wage base)
5. Box 5 >= Box 3            (Medicare has no cap; should be >= SS wages)
```

If any check fails by more than $1, flag for user review.
