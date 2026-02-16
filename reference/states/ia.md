# Iowa State Tax Reference

## Overview

Iowa recently reformed its income tax system, moving to a flat rate that starts from federal taxable income.

| Parameter | Value |
|---|---|
| Tax rate | **3.80%** (flat, 2025) |
| Form | IA 1040 |
| Filing deadline | April 30 (Iowa's deadline is later than most states!) |
| Follows federal AGI? | **No** -- IA starts from federal **taxable income** (Line 15) |
| Standard deduction | **None** (uses federal standard deduction indirectly) |
| Free file available | Yes, via Free File Alliance at https://revenue.iowa.gov/ |

## How IA Tax Works

### Starting Point: Federal Taxable Income (Line 15)

Iowa starts from **federal taxable income** (Form 1040, Line 15), like Colorado, Vermont, and Minnesota. This means the federal standard deduction is already subtracted before Iowa applies its rate.

### No Additional Deduction

Because IA starts after the federal standard deduction, there is no IA-specific standard deduction. The 3.80% rate applies directly to federal taxable income (with Iowa-specific modifications).

### Calculation

```
IA_taxable_income = Federal taxable income (Form 1040, Line 15)
# Iowa-specific adjustments may apply, but minimal for W-2 filers
IA_tax = IA_taxable_income * 0.038
IA_withheld = W-2 Box 17
IA_refund_or_owed = IA_withheld - IA_tax
```

### Sample Calculation (Federal Taxable Income of $27,079)

```
Federal taxable income (Line 15): $27,079.35
IA tax rate:                       × 3.80%
IA tax owed:                       $1,029.02

IA withheld (Box 17):             $X,XXX.XX
IA refund/owed:                   calculated
```

## IA Deductions and Credits

### No State Standard Deduction
Iowa starts from federal taxable income, so the federal standard deduction ($15,750) is already applied.

### Federal Tax Deduction
Iowa previously allowed a deduction for federal income tax paid (like Alabama), but this was **eliminated** as part of the flat tax reform.

### Renter Benefit
IA does **not** offer a general renter's credit or deduction.

### Earned Income Credit
- IA offers its own EIC equal to **15%** of the federal EIC
- If the user qualifies for federal EIC, they also get the IA EIC

### Student Loan Interest
IA does **not** allow a separate student loan interest deduction -- it's already reflected in federal taxable income.

## Filing IA State Return

### IA 1040 Form
1. Go to https://revenue.iowa.gov/ (Free File Alliance partners)
2. **Note: IA deadline is April 30** (not April 15!)
3. Enter federal taxable income (Form 1040, Line 15) as starting point
4. Apply Iowa-specific adjustments
5. Apply 3.80% flat rate
6. Enter withholding from Box 17
7. Calculate refund or amount owed

## What to Tell the User

> "Iowa uses a flat 3.80% rate on your federal taxable income (Line 15, after the standard deduction). This makes Iowa very simple to calculate. Important: Iowa's filing deadline is **April 30**. File via Free File Alliance at revenue.iowa.gov."
