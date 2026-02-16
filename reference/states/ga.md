# Georgia State Tax Reference

## Overview

Georgia recently transitioned from a progressive tax to a flat tax system. For 2025, the flat rate is 5.19% with a $12,000 standard deduction.

| Parameter | Value |
|---|---|
| Tax rate | **5.19%** (flat, 2025; down from 5.39% in 2024) |
| Form | 500 |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- GA starts from federal AGI |
| Standard deduction (Single) | **$12,000** |
| Personal exemption | **None** (repealed in flat tax transition) |
| Free file available | Yes, via Free File Alliance at https://dor.georgia.gov/ |

## How GA Tax Works

### Starting Point: Federal AGI

Georgia begins with federal AGI (Form 1040, Line 11), then applies Georgia Schedule 1 additions and subtractions.

### Standard Deduction

- Single: **$12,000** (2025)
- This was increased as part of the flat tax transition

### Calculation

```
GA_AGI = Federal AGI (Form 1040, Line 11) + GA additions - GA subtractions
# For W-2-only filers, GA AGI typically equals federal AGI
GA_taxable_income = GA_AGI - GA_standard_deduction ($12,000)
GA_taxable_income = max(GA_taxable_income, 0)
GA_tax = GA_taxable_income * 0.0519
GA_withheld = W-2 Box 17
GA_refund_or_owed = GA_withheld - GA_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
GA AGI:                $42,829.35
Standard deduction:   -$12,000.00
GA taxable income:     $30,829.35

GA tax rate:           × 5.19%
GA tax owed:           $1,600.04

GA withheld (Box 17):  $X,XXX.XX
GA refund/owed:        calculated
```

## GA Deductions and Credits

### Standard Deduction
GA offers a $12,000 standard deduction (single). The personal exemption was repealed when Georgia transitioned to the flat tax.

### Renter Benefit
GA does **not** offer a renter's credit or deduction.

### Earned Income Credit
- GA does **not** currently offer its own state EIC

### Student Loan Interest
GA does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

### Low-Income Credit
Georgia offers a low-income tax credit for filers with very low income. Not typically applicable to EZFile's target demographic.

## Filing GA State Return

### Form 500
1. Go to https://dor.georgia.gov/ (Free File Alliance for AGI ≤ $32,000)
2. For higher incomes, approved third-party e-file software
3. Enter federal AGI as starting point
4. Subtract standard deduction ($12,000)
5. Apply 5.19% flat rate
6. Enter withholding from Box 17
7. Calculate refund or amount owed

## What to Tell the User

> "Georgia recently switched to a flat tax system. For 2025, the rate is 5.19% on your federal AGI minus a $12,000 standard deduction. The rate has been declining since the transition. File through Free File Alliance at dor.georgia.gov."
