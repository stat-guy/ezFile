# Washington D.C. Tax Reference

## Overview

Washington D.C. has a progressive income tax with 7 brackets. As a federal district (not a state), D.C. has its own tax authority and filing requirements.

| Parameter | Value |
|---|---|
| Tax type | Progressive (7 brackets) |
| Form | D-40 |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- DC starts from federal AGI |
| Standard deduction (Single) | **$15,750** (matches federal, 2025) |
| Free file available | Yes, at https://otr.cfo.dc.gov/ (MyTax DC) |

## DC Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $10,000 | 4.00% |
| $10,001 - $40,000 | 6.00% |
| $40,001 - $60,000 | 6.50% |
| $60,001 - $250,000 | 8.50% |
| $250,001 - $500,000 | 9.25% |
| $500,001 - $1,000,000 | 9.75% |
| Over $1,000,000 | 10.75% |

**For EZFile's target user:** The first 3-4 brackets (up to $250,000) are most relevant.

### Bracket Computation (Single)

```
if dc_taxable <= 10,000:
    dc_tax = dc_taxable * 0.04
elif dc_taxable <= 40,000:
    dc_tax = 400 + (dc_taxable - 10,000) * 0.06
elif dc_taxable <= 60,000:
    dc_tax = 2,200 + (dc_taxable - 40,000) * 0.065
elif dc_taxable <= 250,000:
    dc_tax = 3,500 + (dc_taxable - 60,000) * 0.085
elif dc_taxable <= 500,000:
    dc_tax = 19,650 + (dc_taxable - 250,000) * 0.0925
elif dc_taxable <= 1,000,000:
    dc_tax = 42,775 + (dc_taxable - 500,000) * 0.0975
else:
    dc_tax = 91,525 + (dc_taxable - 1,000,000) * 0.1075
```

## Calculation

### Step 1: Start from Federal AGI
DC begins with federal AGI (Form 1040, Line 11).

### Step 2: DC Modifications
For W-2-only filers, DC AGI typically equals federal AGI.

### Step 3: DC Standard Deduction
- Single: **$15,750** (2025, matches federal)

### Step 4: DC Taxable Income
```
DC_taxable = DC_AGI - DC_standard_deduction ($15,750)
DC_taxable = max(DC_taxable, 0)
```

### Step 5: Apply Brackets
Use the bracket table above.

### Step 6: Compare to Withholding
```
DC_withheld = W-2 Box 17
DC_refund_or_owed = DC_withheld - DC_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
DC AGI:                $42,829.35
Standard deduction:   -$15,750.00
DC taxable income:     $27,079.35

DC tax calculation:
  4.00% on $10,000:       $400.00
  6.00% on $17,079.35:  $1,024.76
DC tax:                $1,424.76

DC withheld (Box 17):  $X,XXX.XX
DC refund/owed:        calculated
```

## DC Deductions and Credits

### Standard Deduction
DC matches the federal standard deduction ($15,750 single, 2025).

### Schedule H -- Homeowner and Renter Property Tax Credit
- Available to DC renters AND homeowners
- Income limit: AGI ≤ **$66,000** (under age 70) or **$90,000** (age 70+)
- For renters: **20% of annual rent paid** is treated as property tax
- Maximum credit: **$1,425** (2025)
- Can be filed as a standalone form even if no DC tax is owed
- **This applies to EZFile's target user!** Always mention this benefit.

### Earned Income Tax Credit
- DC offers its own EIC equal to **70%** of the federal EIC (one of the most generous)
- If the user qualifies for federal EIC, they also get the DC EIC

### Student Loan Interest
DC does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

## Filing DC Tax Return

### Form D-40
1. Go to https://otr.cfo.dc.gov/ (MyTax DC)
2. Free e-filing available for DC residents
3. Enter federal AGI as starting point
4. Apply standard deduction ($15,750)
5. Calculate tax from DC brackets
6. Check Schedule H renter credit eligibility
7. Enter withholding from Box 17
8. Calculate refund or amount owed

## What to Tell the User

> "D.C. has progressive brackets (4%-10.75%) with a standard deduction matching the federal amount ($15,750). Renters: D.C. offers a property tax credit via Schedule H (20% of rent, up to $1,425) for AGI under $66,000. D.C. also has one of the most generous EICs (70% of federal). File for free at otr.cfo.dc.gov (MyTax DC)."
