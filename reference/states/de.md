# Delaware State Tax Reference

## Overview

Delaware has a progressive income tax with 7 brackets. It has no sales tax, making the income tax the primary state revenue source.

| Parameter | Value |
|---|---|
| Tax type | Progressive (7 brackets) |
| Form | 200-01 (resident) |
| Filing deadline | April 30 (Delaware's deadline is later than most states!) |
| Follows federal AGI? | **Yes** -- DE starts from federal AGI |
| Standard deduction (Single) | **$3,250** |
| Personal credit | **$110** (credit against tax, not a deduction) |
| Free file available | Yes, at https://revenue.delaware.gov/ |

## DE Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $2,000 | 0.00% |
| $2,001 - $5,000 | 2.20% |
| $5,001 - $10,000 | 3.90% |
| $10,001 - $20,000 | 4.80% |
| $20,001 - $25,000 | 5.20% |
| $25,001 - $60,000 | 5.55% |
| Over $60,000 | 6.60% |

**For EZFile's target user:** The first 6 brackets (up to $60,000) are most relevant.

### Bracket Computation (Single)

```
if de_taxable <= 2,000:
    de_tax = 0
elif de_taxable <= 5,000:
    de_tax = (de_taxable - 2,000) * 0.022
elif de_taxable <= 10,000:
    de_tax = 66.00 + (de_taxable - 5,000) * 0.039
elif de_taxable <= 20,000:
    de_tax = 261.00 + (de_taxable - 10,000) * 0.048
elif de_taxable <= 25,000:
    de_tax = 741.00 + (de_taxable - 20,000) * 0.052
elif de_taxable <= 60,000:
    de_tax = 1,001.00 + (de_taxable - 25,000) * 0.0555
else:
    de_tax = 2,943.50 + (de_taxable - 60,000) * 0.066
```

## Calculation

### Step 1: Start from Federal AGI
DE begins with the federal AGI (Form 1040, Line 11).

### Step 2: DE Modifications
For W-2-only filers, DE AGI typically equals federal AGI. Delaware generally conforms to federal definitions.

### Step 3: DE Standard Deduction
- Single: **$3,250**

### Step 4: DE Taxable Income
```
DE_taxable = DE_AGI - DE_standard_deduction ($3,250)
DE_taxable = max(DE_taxable, 0)
```

### Step 5: Apply Brackets
Use the bracket table above.

### Step 6: Personal Credit
- Single: **$110** (subtracted from tax, not income)

### Step 7: Final DE Tax
```
DE_tax = bracket_tax - personal_credit ($110)
DE_tax = max(DE_tax, 0)
```

### Step 8: Compare to Withholding
```
DE_withheld = W-2 Box 17
DE_refund_or_owed = DE_withheld - DE_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
DE AGI:                $42,829.35
Standard deduction:    -$3,250.00
DE taxable income:     $39,579.35

DE tax calculation:
  0.00% on $2,000:         $0.00
  2.20% on $3,000:        $66.00
  3.90% on $5,000:       $195.00
  4.80% on $10,000:      $480.00
  5.20% on $5,000:       $260.00
  5.55% on $14,579.35:   $809.15
DE gross tax:          $1,810.15
Personal credit:        -$110.00
DE net tax:            $1,700.15

DE withheld (Box 17):  $X,XXX.XX
DE refund/owed:        calculated
```

## DE Deductions and Credits

### Standard Deduction
DE offers a $3,250 standard deduction -- lower than most states and significantly lower than the federal amount.

### Personal Credit
The $110 personal credit reduces tax owed (not taxable income).

### Renter Benefit
DE does **not** offer a renter's credit or deduction.

### Earned Income Credit
- DE does **not** currently offer its own state EIC

### Student Loan Interest
DE does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

### No Sales Tax Note
Delaware has no sales tax, which is a notable financial benefit but doesn't affect the income tax return.

## Filing DE State Return

### Form 200-01
1. Go to https://revenue.delaware.gov/
2. Free e-filing available for DE residents
3. **Note: DE deadline is April 30** (not April 15!)
4. Enter federal AGI as starting point
5. Subtract standard deduction ($3,250)
6. Calculate tax from DE brackets
7. Subtract personal credit ($110)
8. Enter withholding from Box 17
9. Calculate refund or amount owed

## What to Tell the User

> "Delaware has progressive brackets (0%-6.60%) with a $3,250 standard deduction and a $110 personal credit. The first $2,000 of taxable income is tax-free. While Delaware has no sales tax, the income tax is straightforward. Important: Delaware's filing deadline is **April 30**. File for free at revenue.delaware.gov."
