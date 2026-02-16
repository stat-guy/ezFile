# South Carolina State Tax Reference

## Overview

South Carolina has a progressive income tax with 3 simplified brackets. SC starts from **federal taxable income** (Line 15), not federal AGI, and applies its own standard deduction.

| Parameter | Value |
|---|---|
| Tax type | Progressive (3 brackets) |
| Form | SC1040 |
| Filing deadline | April 15 |
| Follows federal AGI? | **No** -- SC starts from federal **taxable income** (Line 15) |
| Standard deduction (Single) | **$15,000** (SC's own deduction, applied after adjustments) |
| Free file available | Yes, via approved e-file software at https://dor.sc.gov/ |

## SC Tax Brackets (All Filing Statuses, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $3,560 | 0% |
| $3,561 - $17,830 | 3% |
| Over $17,830 | 6% |

**For EZFile's target user:** Most income above the 0% bracket falls in the 6% bracket.

### Bracket Computation

```
if sc_taxable <= 3,560:
    sc_tax = 0
elif sc_taxable <= 17,830:
    sc_tax = (sc_taxable - 3,560) * 0.03
else:
    sc_tax = 428.10 + (sc_taxable - 17,830) * 0.06
```

## How SC Tax Works

### Starting Point: Federal Taxable Income (Line 15)

South Carolina starts from **federal taxable income** (Form 1040, Line 15), which already has the federal standard deduction subtracted. SC then adds back the federal deduction and applies its own $15,000 standard deduction through the adjustment process.

### Understanding the Add-Back Process

Because SC starts from federal taxable income (which already removed the federal $15,750 standard deduction), SC effectively:
1. Starts with federal Line 15
2. Adds back certain items via SC Schedule
3. Subtracts SC's own standard deduction ($15,000)

For a simple W-2 filer, the net effect is approximately:
```
SC_taxable ≈ Federal AGI - SC_standard_deduction ($15,000)
```

### Simplified Calculation (For W-2-Only Filers)

```
SC_starting_income = Federal taxable income (Form 1040, Line 15)
# Add back federal standard deduction, subtract SC standard deduction
# Net adjustment ≈ +$15,750 (federal) - $15,000 (SC) = +$750
SC_taxable_income = SC_starting_income + $750 (approximately)
SC_taxable_income = max(SC_taxable_income, 0)
SC_tax = apply brackets to SC_taxable_income
SC_withheld = W-2 Box 17
SC_refund_or_owed = SC_withheld - SC_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
Federal taxable income (Line 15): $27,079.35
Add back federal std deduction:   +$15,750.00
Subtract SC std deduction:       -$15,000.00
SC taxable income:                $27,829.35

SC tax calculation:
  0% on $3,560:                $0.00
  3% on $14,270:             $428.10
  6% on $9,999.35:           $599.96
SC tax:                     $1,028.06

SC withheld (Box 17):       $X,XXX.XX
SC refund/owed:             calculated
```

## SC Deductions and Credits

### Standard Deduction
SC offers a $15,000 standard deduction (single). This is close to the federal amount but applied through SC's own process since the starting point is federal taxable income.

### Renter Benefit
SC does **not** offer a renter's credit or deduction.

### Earned Income Credit
- SC does **not** currently offer its own state EIC

### Student Loan Interest
SC does **not** allow a separate student loan interest deduction -- it's already reflected in the federal starting point.

### Two-Wage Earner Credit
Available to married couples only -- NOT applicable to EZFile's single filer profile.

## Filing SC State Return

### SC1040 Form
1. Go to https://dor.sc.gov/
2. Free e-filing via approved third-party software (income ≤ $89,000)
3. Enter federal taxable income (Form 1040, Line 15) as starting point
4. Apply SC adjustments (add back federal deduction, subtract SC deduction)
5. Calculate tax from SC brackets
6. Enter withholding from Box 17
7. Calculate refund or amount owed

## What to Tell the User

> "South Carolina has three brackets (0%, 3%, and 6%) with a $15,000 standard deduction. SC starts from your federal taxable income rather than AGI, then makes adjustments. The first $3,560 of SC taxable income is tax-free. File for free through approved e-file software at dor.sc.gov."
