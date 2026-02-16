# Kentucky State Tax Reference

## Overview

Kentucky has a simple flat income tax that has been declining via automatic triggers. The rate dropped to 3.5% effective 2026, but for tax year 2025 it remains at 4.0%.

| Parameter | Value |
|---|---|
| Tax rate | **4.0%** (flat, 2025) |
| Form | 740 |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- KY starts from federal AGI |
| Standard deduction (Single) | **$3,270** |
| Personal exemption | **None** |
| Free file available | Yes, at https://mytaxes.ky.gov/ (KY File) |

## How KY Tax Works

### Starting Point: Federal AGI

Kentucky begins with federal AGI (Form 1040, Line 11), then applies Kentucky-specific additions and subtractions.

### Standard Deduction

- Single: **$3,270** (2025)
- This is significantly lower than the federal standard deduction

### Calculation

```
KY_AGI = Federal AGI (Form 1040, Line 11)
# For W-2-only filers, KY AGI typically equals federal AGI
KY_taxable_income = KY_AGI - KY_standard_deduction ($3,270)
KY_taxable_income = max(KY_taxable_income, 0)
KY_tax = KY_taxable_income * 0.04
KY_withheld = W-2 Box 17
KY_refund_or_owed = KY_withheld - KY_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
KY AGI:                $42,829.35
Standard deduction:    -$3,270.00
KY taxable income:     $39,559.35

KY tax rate:           × 4.0%
KY tax owed:           $1,582.37

KY withheld (Box 17):  $X,XXX.XX
KY refund/owed:        calculated
```

## KY Deductions and Credits

### Standard Deduction
KY's standard deduction ($3,270 single) is quite low compared to most states. This means KY taxes a larger portion of income.

### Family Size Tax Credit
- Available to very low-income filers (income up to 133% of federal poverty level)
- Not typically applicable to W-2 filers in EZFile's target demographic

### Renter Benefit
KY does **not** offer a renter's credit or deduction.

### Earned Income Credit
- KY does **not** currently offer its own state EIC

### Student Loan Interest
KY does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

## Filing KY State Return

### Form 740
1. Go to https://mytaxes.ky.gov/ (KY File -- free for all KY residents)
2. Complete your federal return first
3. Enter federal AGI as starting point
4. Subtract standard deduction ($3,270)
5. Apply 4.0% flat rate
6. Enter withholding from Box 17
7. Calculate refund or amount owed

## What to Tell the User

> "Kentucky uses a flat 4.0% rate on your federal AGI minus a $3,270 standard deduction. The rate has been declining and drops to 3.5% in 2026. File for free at mytaxes.ky.gov -- Kentucky offers free filing for all residents with no income limit."
