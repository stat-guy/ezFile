# Missouri State Tax Reference

## Overview

Missouri has a progressive income tax with narrow brackets that quickly reach the top rate. The top rate has been declining gradually.

| Parameter | Value |
|---|---|
| Tax type | Progressive (multiple narrow brackets) |
| Form | MO-1040 |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- MO starts from federal AGI |
| Standard deduction (Single) | **$15,750** (matches federal, 2025) |
| Free file available | Yes, at https://dor.mo.gov/ (MO Free File) |

## MO Tax Brackets (Single, 2025 Estimated)

| Taxable Income | Rate |
|---|---|
| $0 - $1,313 | 0% |
| $1,208 - $2,626 | 2.0% |
| $2,415 - $3,939 | 2.5% |
| $3,622 - $5,252 | 3.0% |
| $4,829 - $6,565 | 3.5% |
| $6,036 - $7,878 | 4.0% |
| $7,243 - $9,191 | 4.5% |
| Over $9,191 | 4.70% |

**Key insight:** The top rate (4.70%) kicks in at just $9,192. For most W-2 filers, the effective rate is very close to 4.70%.

### Bracket Computation (Simplified)

```
if mo_taxable <= 1,207:
    mo_tax = 0
elif mo_taxable <= 2,414:
    mo_tax = (mo_taxable - 1,207) * 0.02
elif mo_taxable <= 3,621:
    mo_tax = 24.14 + (mo_taxable - 2,414) * 0.025
# ... (additional narrow brackets)
elif mo_taxable > 8,449:
    # Simplified: accumulate ~$153 from lower brackets, then 4.70% on rest
    mo_tax = 153.30 + (mo_taxable - 8,449) * 0.047
```

## Calculation

### Step 1: Start from Federal AGI
MO begins with federal AGI (Form 1040, Line 11).

### Step 2: MO Standard Deduction
- Single: **$15,750** (matches federal, 2025)

### Step 3: MO Taxable Income
```
MO_taxable = MO_AGI - MO_standard_deduction ($15,750)
MO_taxable = max(MO_taxable, 0)
```

### Step 4: Apply Brackets

### Step 5: Compare to Withholding
```
MO_withheld = W-2 Box 17
MO_refund_or_owed = MO_withheld - MO_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
MO AGI:                $42,829.35
Standard deduction:   -$15,750.00
MO taxable income:     $27,079.35

MO tax (simplified):
  Lower brackets:        ~$153.30
  4.70% on $18,630.35:   $875.63
MO tax:                ~$1,028.93

MO withheld (Box 17):  $X,XXX.XX
MO refund/owed:        calculated
```

## MO Deductions and Credits

### Standard Deduction
MO matches the federal standard deduction ($15,750 single, 2025).

### Renter Benefit
MO offers a **Property Tax Credit** for renters who are **65+ or disabled** with income below ~$30,000. NOT applicable to most EZFile users.

### Earned Income Credit
- MO does **not** currently offer its own state EIC

### Student Loan Interest
MO does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

## Filing MO State Return

### MO-1040 Form
1. Go to https://dor.mo.gov/ (MO Free File)
2. Free e-filing available for MO residents
3. Enter federal AGI as starting point
4. Apply standard deduction ($15,750)
5. Calculate tax from MO brackets
6. Enter withholding from Box 17
7. Calculate refund or amount owed

## What to Tell the User

> "Missouri has many narrow brackets but the top rate (4.70%) kicks in at just $9,192, so most of your income is effectively at 4.70%. The standard deduction matches federal ($15,750). File for free at dor.mo.gov."
