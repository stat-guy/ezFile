# Illinois State Tax Reference

## Overview

Illinois has a simple flat income tax rate applied to federal AGI with no standard deduction -- just a personal exemption.

| Parameter | Value |
|---|---|
| Tax rate | **4.95%** (flat) |
| Form | IL-1040 |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- IL starts from federal AGI |
| Standard deduction | **None** |
| Personal exemption | **$2,850** (2025, single) |
| Free file available | Yes, at https://mytax.illinois.gov/ |

## How IL Tax Works

### Starting Point: Federal AGI

Illinois begins with federal AGI (Form 1040, Line 11). There are very few IL-specific additions or subtractions for W-2-only filers.

### Personal Exemption

IL does not have a standard deduction. Instead, it offers a flat personal exemption:
- Single: **$2,850** (2025)
- This reduces taxable income (not a credit)

### Calculation

```
IL_AGI = Federal AGI (Form 1040, Line 11)
IL_taxable_income = IL_AGI - personal_exemption ($2,850)
IL_taxable_income = max(IL_taxable_income, 0)
IL_tax = IL_taxable_income * 0.0495
IL_withheld = W-2 Box 17
IL_refund_or_owed = IL_withheld - IL_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
IL AGI:                $42,829.35
Personal exemption:    -$2,850.00
IL taxable income:     $39,979.35

IL tax rate:           × 4.95%
IL tax owed:           $1,978.98

IL withheld (Box 17):  $X,XXX.XX
IL refund/owed:        calculated
```

## IL Deductions and Credits

### No Standard Deduction
IL does NOT offer a standard deduction. The 4.95% rate applies to AGI minus the personal exemption only.

### Property Tax Credit
- For homeowners only -- NOT applicable to EZFile's target user (renters)

### Earned Income Credit
- IL offers its own EIC equal to 20% of the federal EIC
- If the user qualifies for federal EIC, they also get the IL EIC

### Student Loan Interest
IL does **not** allow a separate student loan interest deduction at the state level -- it's already reflected in federal AGI.

### Renter Benefit
IL does **not** offer a renter's credit or deduction.

## Filing IL State Return

### IL-1040 Form
1. Go to https://mytax.illinois.gov/
2. Free e-filing available for IL residents
3. Enter federal AGI as starting point
4. Subtract personal exemption ($2,850)
5. Apply 4.95% flat rate
6. Enter withholding from Box 17
7. Calculate refund or amount owed

## What to Tell the User

> "Illinois uses a flat 4.95% tax rate on your federal AGI minus a $2,850 personal exemption. No brackets, no standard deduction -- simple and straightforward. File for free at mytax.illinois.gov."
