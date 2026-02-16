# Virginia State Tax Reference

## Overview

Virginia has a progressive income tax with 4 brackets. Most W-2 filers hit the top bracket (5.75%) quickly since it starts at just $17,001.

| Parameter | Value |
|---|---|
| Tax type | Progressive (4 brackets) |
| Form | 760 (resident) |
| Filing deadline | May 1 (Virginia's deadline is later than most states!) |
| Follows federal AGI? | **Yes** -- VA starts from federal AGI |
| Standard deduction (Single) | **$8,000** |
| Personal exemption | **$930** |
| Free file available | Yes, at https://www.tax.virginia.gov/ (Virginia Free File) |

## VA Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $3,000 | 2.00% |
| $3,001 - $5,000 | 3.00% |
| $5,001 - $17,000 | 5.00% |
| Over $17,000 | 5.75% |

**Key insight:** The top rate kicks in at just $17,001. For most W-2 filers, the effective rate is very close to 5.75% on nearly all income above the standard deduction.

### Bracket Computation (Single)

```
if va_taxable <= 3,000:
    va_tax = va_taxable * 0.02
elif va_taxable <= 5,000:
    va_tax = 60 + (va_taxable - 3,000) * 0.03
elif va_taxable <= 17,000:
    va_tax = 120 + (va_taxable - 5,000) * 0.05
else:
    va_tax = 720 + (va_taxable - 17,000) * 0.0575
```

## Calculation

### Step 1: Start from Federal AGI
VA begins with the federal AGI (Form 1040, Line 11).

### Step 2: VA Modifications
For W-2-only filers, VA AGI typically equals federal AGI.

### Step 3: VA Standard Deduction and Exemption
- Standard deduction (Single): **$8,000**
- Personal exemption: **$930** (subtracted from income, not a credit)
- Total deductions from income: $8,000 + $930 = **$8,930**

### Step 4: VA Taxable Income
```
VA_taxable = VA_AGI - VA_standard_deduction ($8,000) - VA_personal_exemption ($930)
VA_taxable = max(VA_taxable, 0)
```

### Step 5: Apply Brackets
Use the bracket table above.

### Step 6: Compare to Withholding
```
VA_withheld = W-2 Box 17
VA_refund_or_owed = VA_withheld - VA_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
VA AGI:                $42,829.35
Standard deduction:    -$8,000.00
Personal exemption:      -$930.00
VA taxable income:     $33,899.35

VA tax calculation:
  2.00% on $3,000:         $60.00
  3.00% on $2,000:         $60.00
  5.00% on $12,000:       $600.00
  5.75% on $16,899.35:    $971.71
VA tax:                $1,691.71

VA withheld (Box 17):  $X,XXX.XX
VA refund/owed:        calculated
```

## VA Deductions and Credits

### Standard Deduction + Personal Exemption
VA provides both a standard deduction ($8,000) and a personal exemption ($930). Together they reduce taxable income by $8,930.

### Renter Benefit
VA does **not** offer a general renter's credit or deduction. An age-based credit exists for residents age **65 or older** only.

### Earned Income Credit
- VA offers its own EIC equal to **20%** of the federal EIC (refundable)
- If the user qualifies for federal EIC, they also get the VA EIC

### Student Loan Interest
VA does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

### Low-Income Credit
VA has a low-income tax credit for filers with federal AGI below ~$12,000 (single). Reduces VA tax to $0.

## Filing VA State Return

### Form 760
1. Go to https://www.tax.virginia.gov/ (Virginia Free File)
2. Free e-filing available for VA residents
3. **Note: VA deadline is May 1** (not April 15!)
4. Enter federal AGI as starting point
5. Subtract standard deduction ($8,000) and personal exemption ($930)
6. Calculate tax from VA brackets
7. Enter withholding from Box 17
8. Calculate refund or amount owed

## What to Tell the User

> "Virginia has progressive brackets but the top rate (5.75%) kicks in at just $17,001 of taxable income, so most filers are effectively at 5.75%. VA gives you an $8,000 standard deduction plus a $930 personal exemption. Important: Virginia's filing deadline is **May 1**, not April 15. File for free at tax.virginia.gov."
