# Arizona State Tax Reference

## Overview

Arizona has a simple flat income tax rate with a standard deduction that matches the federal amount.

| Parameter | Value |
|---|---|
| Tax rate | **2.50%** (flat) |
| Form | 140 (resident) |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- AZ starts from federal AGI |
| Standard deduction (Single) | **$15,750** (matches federal, 2025) |
| Free file available | Yes, at https://azdor.gov/ (AZTaxes) |

## How AZ Tax Works

### Starting Point: Federal AGI

Arizona begins with federal AGI (Form 1040, Line 11).

### Standard Deduction

AZ adopted the same standard deduction as the federal amount:
- Single: **$15,750** (2025)
- Single 65+: **$17,750** (2025)

### Calculation

```
AZ_AGI = Federal AGI (Form 1040, Line 11)
AZ_taxable_income = AZ_AGI - AZ_standard_deduction ($15,750)
AZ_taxable_income = max(AZ_taxable_income, 0)
AZ_tax = AZ_taxable_income * 0.025
AZ_withheld = W-2 Box 17
AZ_refund_or_owed = AZ_withheld - AZ_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
AZ AGI:                $42,829.35
Standard deduction:   -$15,750.00
AZ taxable income:     $27,079.35

AZ tax rate:           × 2.50%
AZ tax owed:             $676.98

AZ withheld (Box 17):  $X,XXX.XX
AZ refund/owed:        calculated
```

## AZ Deductions and Credits

### Standard Deduction
AZ uses the same standard deduction as the federal government ($15,750 single, $17,750 single 65+). This makes the starting taxable income identical to the federal amount.

### Property Tax Credit
- For homeowners only -- NOT applicable to EZFile's target user (renters)

### Renter Benefit
- AZ does **not** offer a general renter's credit or deduction
- A property tax credit exists for residents age **65 or older** only

### Family Income Tax Credit
- $40 for single filers with income under $10,000
- Unlikely for most W-2 filers in EZFile's target demographic

### Earned Income Tax Credit
- AZ does **not** currently offer its own state EIC

### Student Loan Interest
AZ does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

## Filing AZ State Return

### Form 140
1. Go to https://azdor.gov/ (AZTaxes)
2. Free e-filing available for AZ residents
3. Enter federal AGI as starting point
4. Subtract standard deduction ($15,750)
5. Apply 2.50% flat rate
6. Enter withholding from Box 17
7. Calculate refund or amount owed

## What to Tell the User

> "Arizona uses a flat 2.50% tax rate -- one of the lowest in the country. Your AZ standard deduction ($15,750) matches the federal amount, so your AZ taxable income is the same as your federal taxable income. File for free at azdor.gov."
