# Nebraska State Tax Reference

## Overview

Nebraska has a progressive income tax with 4 brackets. Rates have been declining in recent years through tax reform legislation.

| Parameter | Value |
|---|---|
| Tax type | Progressive (4 brackets) |
| Form | 1040N |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- NE starts from federal AGI |
| Standard deduction (Single) | **$8,600** (2025) |
| Personal exemption credit | **$171** per exemption (nonrefundable credit) |
| Free file available | Yes, at https://revenue.nebraska.gov/ (NebFile) |

## NE Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $4,030 | 2.46% |
| $4,031 - $24,120 | 3.51% |
| $24,121 - $38,870 | 5.01% |
| Over $38,870 | 5.20% |

### Bracket Computation (Single)

```
if ne_taxable <= 4,030:
    ne_tax = ne_taxable * 0.0246
elif ne_taxable <= 24,120:
    ne_tax = 99.14 + (ne_taxable - 4,030) * 0.0351
elif ne_taxable <= 38,870:
    ne_tax = 803.30 + (ne_taxable - 24,120) * 0.0501
else:
    ne_tax = 1,541.26 + (ne_taxable - 38,870) * 0.052
```

## Calculation

### Step 1: Start from Federal AGI
NE begins with federal AGI (Form 1040, Line 11).

### Step 2: NE Standard Deduction
- Single: **$8,600** (2025)

### Step 3: NE Taxable Income
```
NE_taxable = NE_AGI - NE_standard_deduction ($8,600)
NE_taxable = max(NE_taxable, 0)
```

### Step 4: Apply Brackets

### Step 5: Personal Exemption Credit
- **$171** per exemption (nonrefundable, reduces tax not income)

### Step 6: Compare to Withholding
```
NE_tax = bracket_tax - personal_credit ($171)
NE_tax = max(NE_tax, 0)
NE_withheld = W-2 Box 17
NE_refund_or_owed = NE_withheld - NE_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
NE AGI:                $42,829.35
Standard deduction:    -$8,600.00
NE taxable income:     $34,229.35

NE tax calculation:
  2.46% on $4,030:        $99.14
  3.51% on $20,090:      $705.16
  5.01% on $10,109.35:   $506.48
NE gross tax:          $1,310.78
Personal credit:          -$171.00
NE net tax:            $1,139.78

NE withheld (Box 17):  $X,XXX.XX
NE refund/owed:        calculated
```

## NE Deductions and Credits

### Standard Deduction
NE offers an $8,600 standard deduction (single, 2025).

### Personal Exemption Credit
The $171 credit reduces tax owed (not taxable income).

### Renter Benefit
NE does **not** offer a general renter's credit or deduction. A Property Tax Credit exists for homeowners.

### Earned Income Credit
- NE offers its own EIC equal to **10%** of the federal EIC (refundable)
- If the user qualifies for federal EIC, they also get the NE EIC

### Student Loan Interest
NE does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

## Filing NE State Return

### Form 1040N
1. Go to https://revenue.nebraska.gov/ (NebFile -- free for all NE residents)
2. Enter federal AGI as starting point
3. Subtract standard deduction ($8,600)
4. Calculate tax from NE brackets
5. Subtract $171 personal credit
6. Enter withholding from Box 17
7. Calculate refund or amount owed

## What to Tell the User

> "Nebraska has progressive brackets (2.46%-5.20%) with an $8,600 standard deduction and a $171 personal exemption credit. Rates have been declining and may drop further. File for free at revenue.nebraska.gov using NebFile."
