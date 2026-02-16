# Rhode Island State Tax Reference

## Overview

Rhode Island has a progressive income tax with 3 brackets and a standard deduction.

| Parameter | Value |
|---|---|
| Tax type | Progressive (3 brackets) |
| Form | RI-1040 |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- RI starts from federal AGI |
| Standard deduction (Single) | **$10,900** (2025) |
| Free file available | Yes, at https://www.tax.ri.gov/ |

## RI Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $77,450 | 3.75% |
| $77,451 - $176,050 | 4.75% |
| Over $176,050 | 5.99% |

**For EZFile's target user:** The first bracket (up to $77,450) covers most filers.

### Bracket Computation (Single)

```
if ri_taxable <= 77,450:
    ri_tax = ri_taxable * 0.0375
elif ri_taxable <= 176,050:
    ri_tax = 2,904.38 + (ri_taxable - 77,450) * 0.0475
else:
    ri_tax = 7,588.00 + (ri_taxable - 176,050) * 0.0599
```

## Calculation

### Step 1: Start from Federal AGI
RI begins with the federal AGI (Form 1040, Line 11).

### Step 2: RI Modifications
For W-2-only filers, RI AGI typically equals federal AGI. RI has some modifications but they rarely apply to simple W-2 filers.

### Step 3: RI Standard Deduction
- Single: **$10,900** (2025)
- This is lower than the federal standard deduction

### Step 4: RI Taxable Income
```
RI_taxable = RI_AGI - RI_standard_deduction ($10,900)
RI_taxable = max(RI_taxable, 0)
```

### Step 5: Apply Brackets
Use the bracket table above.

### Step 6: Compare to Withholding
```
RI_withheld = W-2 Box 17
RI_refund_or_owed = RI_withheld - RI_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
RI AGI:                $42,829.35
Standard deduction:   -$10,900.00
RI taxable income:     $31,929.35

RI tax calculation:
  3.75% on $31,929.35:  $1,197.35
RI tax:                $1,197.35

RI withheld (Box 17):  $X,XXX.XX
RI refund/owed:        calculated
```

## RI Deductions and Credits

### Standard Deduction
RI offers a $10,900 standard deduction (single). This is lower than the federal amount but higher than some states.

### Property Tax Credit
- Available to homeowners and renters, but ONLY for **age 65+ or disabled** residents
- NOT applicable to most of EZFile's target users

### Renter Benefit
- RI does **not** offer a general renter's credit or deduction for non-elderly/non-disabled filers
- The property tax credit for 65+ residents covers renters

### Earned Income Credit
- RI offers its own EIC equal to **16%** of the federal EIC
- If the user qualifies for federal EIC, they also get the RI EIC

### Student Loan Interest
RI does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

## Filing RI State Return

### RI-1040 Form
1. Go to https://www.tax.ri.gov/
2. Free e-filing available for RI residents
3. Enter federal AGI as starting point
4. Apply standard deduction ($10,900)
5. Calculate tax from RI brackets
6. Enter withholding from Box 17
7. Calculate refund or amount owed

## What to Tell the User

> "Rhode Island has three tax brackets (3.75%, 4.75%, and 5.99%) with a $10,900 standard deduction. At most income levels for EZFile's target demographic, you'll likely be in the 3.75% bracket. File for free at tax.ri.gov."
