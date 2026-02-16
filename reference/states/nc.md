# North Carolina State Tax Reference

## Overview

North Carolina has a simple flat income tax rate that has been declining steadily and is one of the lower flat rates in the country.

| Parameter | Value |
|---|---|
| Tax rate | **4.25%** (flat, 2025; down from 4.50% in 2024, heading to 3.99% in 2026) |
| Form | D-400 |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- NC starts from federal AGI |
| Standard deduction (Single) | **$12,750** |
| Free file available | Yes, via NC Free File at https://www.ncdor.gov/ |

## How NC Tax Works

### Starting Point: Federal AGI

North Carolina begins with federal AGI (Form 1040, Line 11), then applies NC-specific adjustments via Schedule S to arrive at NC AGI.

### Standard Deduction

NC uses its own standard deduction (not the federal amount):
- Single: **$12,750** (2025)

### Calculation

```
NC_AGI = Federal AGI (Form 1040, Line 11) + NC additions - NC subtractions
# For W-2-only filers, NC AGI typically equals federal AGI
NC_taxable_income = NC_AGI - NC_standard_deduction ($12,750)
NC_taxable_income = max(NC_taxable_income, 0)
NC_tax = NC_taxable_income * 0.0425
NC_withheld = W-2 Box 17
NC_refund_or_owed = NC_withheld - NC_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
NC AGI:                $42,829.35
Standard deduction:   -$12,750.00
NC taxable income:     $30,079.35

NC tax rate:           × 4.25%
NC tax owed:           $1,278.37

NC withheld (Box 17):  $X,XXX.XX
NC refund/owed:        calculated
```

## NC Deductions and Credits

### Standard Deduction
NC offers a $12,750 standard deduction. While lower than the federal amount ($15,750), it's relatively generous compared to many states.

### Renter Benefit
NC does **not** offer a renter's credit or deduction.

### Earned Income Credit
- NC does **not** currently offer its own state EIC

### Student Loan Interest
NC does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

### Child Deduction
$2,500 per qualifying child -- NOT applicable to EZFile's target user (no dependents).

## Filing NC State Return

### Form D-400
1. Go to https://www.ncdor.gov/ (NC Free File)
2. Free e-filing available through approved third-party software
3. Enter federal AGI as starting point
4. Apply NC standard deduction ($12,750)
5. Apply 4.25% flat rate
6. Enter withholding from Box 17
7. Calculate refund or amount owed

## What to Tell the User

> "North Carolina uses a flat 4.25% rate (one of the lowest flat rates) on your federal AGI minus a $12,750 standard deduction. The rate has been declining each year and drops to 3.99% in 2026. File for free via NC Free File at ncdor.gov."
