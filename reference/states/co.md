# Colorado State Tax Reference

## Overview

Colorado has a simple flat income tax, but uniquely starts from **federal taxable income** (Form 1040 Line 15) rather than federal AGI.

| Parameter | Value |
|---|---|
| Tax rate | **4.40%** (flat) |
| Form | DR 0104 |
| Filing deadline | April 15 |
| Follows federal AGI? | **No** -- CO starts from federal **taxable income** (Line 15) |
| Standard deduction | **None** (uses federal standard deduction indirectly) |
| Free file available | Yes, at https://tax.colorado.gov/ (Revenue Online) |

## How CO Tax Works

### Starting Point: Federal Taxable Income (Line 15)

Unlike most states that start from federal AGI (Line 11), Colorado starts from **federal taxable income** (Form 1040, Line 15). This means the federal standard deduction is already subtracted before Colorado even begins its calculation.

This makes Colorado's effective calculation very simple for W-2-only filers.

### No Additional Deduction

Because CO starts after the federal standard deduction, there is no CO-specific standard deduction or personal exemption to subtract. The 4.40% rate applies directly to federal taxable income.

### Calculation

```
CO_taxable_income = Federal taxable income (Form 1040, Line 15)
CO_tax = CO_taxable_income * 0.044
CO_withheld = W-2 Box 17
CO_refund_or_owed = CO_withheld - CO_tax
```

### Sample Calculation (Federal Taxable Income of $27,079)

```
Federal taxable income (Line 15): $27,079.35
CO tax rate:                       × 4.40%
CO tax owed:                       $1,191.49

CO withheld (Box 17):             $X,XXX.XX
CO refund/owed:                   calculated
```

## CO Deductions and Credits

### No Standard Deduction
CO does NOT offer its own standard deduction. Because it starts from federal taxable income, the federal standard deduction ($15,750) is already applied.

### Property Tax/Rent/Heat Rebate (PTC)
- Available ONLY to residents age **65 or older**, surviving spouses 58+, or disabled
- NOT applicable to most of EZFile's target users
- If eligible: rebate on property tax, rent, and heating costs

### Earned Income Tax Credit (CO EITC)
- CO offers its own EITC equal to **25%** of the federal EIC (2025)
- If the user qualifies for federal EIC, they also get the CO EITC
- Refundable credit

### Student Loan Interest
CO does **not** allow a separate student loan interest deduction -- it's already reflected in federal taxable income (which started from AGI minus deductions).

### Renter Benefit
CO does **not** offer a general renter's credit or deduction. The PTC rebate is restricted to age 65+ or disabled.

## Filing CO State Return

### DR 0104 Form
1. Go to https://tax.colorado.gov/ (Revenue Online)
2. Free e-filing available for CO residents
3. Enter federal taxable income (Form 1040, Line 15) as starting point
4. Apply 4.40% flat rate
5. Enter withholding from Box 17
6. Check CO EITC eligibility if applicable
7. Calculate refund or amount owed

## What to Tell the User

> "Colorado uses a flat 4.40% rate on your federal taxable income -- that's Line 15, after your standard deduction is already subtracted. This makes CO one of the simplest state returns to calculate. File for free at tax.colorado.gov."
