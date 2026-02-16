# Arkansas State Tax Reference

## Overview

Arkansas has a progressive income tax with 5 brackets that has been declining rapidly. The top rate dropped to 3.9% for 2025.

| Parameter | Value |
|---|---|
| Tax type | Progressive (5 brackets) |
| Form | AR1000F |
| Filing deadline | April 15 |
| Follows federal AGI? | **Partially** -- AR has its own AGI definition but is close to federal for W-2 filers |
| Standard deduction (Single) | **$2,470** (2025) |
| Personal tax credit | **$29** (credit against tax, not a deduction) |
| Free file available | Yes, at https://atap.arkansas.gov/ (ATAP) |

## AR Tax Brackets (Single, Net Income ≤ $92,300, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $5,499 | 0.00% |
| $5,500 - $10,899 | 2.00% |
| $10,900 - $15,599 | 3.00% |
| $15,600 - $25,699 | 3.40% |
| Over $25,700 | 3.90% |

**For EZFile's target user:** All 5 brackets apply. The 0% bracket on the first $5,499 effectively acts as additional tax-free income.

### Bracket Computation (Single, Net Income ≤ $92,300)

```
if ar_taxable <= 5,499:
    ar_tax = 0
elif ar_taxable <= 10,899:
    ar_tax = (ar_taxable - 5,500) * 0.02
elif ar_taxable <= 15,599:
    ar_tax = 107.98 + (ar_taxable - 10,900) * 0.03
elif ar_taxable <= 25,699:
    ar_tax = 248.95 + (ar_taxable - 15,600) * 0.034
else:
    ar_tax = 592.31 + (ar_taxable - 25,700) * 0.039
```

## Calculation

### Step 1: Start from AR AGI
AR has its own AGI definition but for simple W-2 filers, it's very close to federal AGI.

### Step 2: AR Standard Deduction
- Single: **$2,470** (2025)

### Step 3: AR Taxable Income
```
AR_taxable = AR_AGI - AR_standard_deduction ($2,470)
AR_taxable = max(AR_taxable, 0)
```

### Step 4: Apply Brackets
Use the bracket table above.

### Step 5: Personal Tax Credit
- **$29** per person (subtracted from tax, not income)

### Step 6: Compare to Withholding
```
AR_tax = bracket_tax - personal_credit ($29)
AR_tax = max(AR_tax, 0)
AR_withheld = W-2 Box 17
AR_refund_or_owed = AR_withheld - AR_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
AR AGI:                $42,829.35
Standard deduction:    -$2,470.00
AR taxable income:     $40,359.35

AR tax calculation:
  0.00% on $5,499:         $0.00
  2.00% on $5,400:       $108.00
  3.00% on $4,700:       $141.00
  3.40% on $10,100:      $343.40
  3.90% on $14,659.35:   $571.71
AR gross tax:          $1,164.11
Personal credit:          -$29.00
AR net tax:            $1,135.11

AR withheld (Box 17):  $X,XXX.XX
AR refund/owed:        calculated
```

## AR Deductions and Credits

### Standard Deduction
AR offers a $2,470 standard deduction (single). Relatively low.

### Renter Benefit
AR does **not** offer a renter's credit or deduction.

### Earned Income Credit
- AR does **not** currently offer its own state EIC

### Student Loan Interest
AR does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

## Filing AR State Return

### Form AR1000F
1. Go to https://atap.arkansas.gov/ (ATAP)
2. Free e-filing available for AR residents
3. Enter AR AGI (approximately federal AGI for W-2 filers)
4. Subtract standard deduction ($2,470)
5. Calculate tax from brackets
6. Subtract $29 personal credit
7. Enter withholding from Box 17
8. Calculate refund or amount owed

## What to Tell the User

> "Arkansas has progressive brackets with the first $5,499 tax-free and a top rate of just 3.9% (one of the lower top rates). Standard deduction is $2,470 and you get a small $29 personal credit. File for free at atap.arkansas.gov."
