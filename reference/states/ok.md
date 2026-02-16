# Oklahoma State Tax Reference

## Overview

Oklahoma has a progressive income tax with 6 narrow brackets that quickly reach the top rate.

| Parameter | Value |
|---|---|
| Tax type | Progressive (6 brackets) |
| Form | 511 (resident) |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- OK starts from federal AGI |
| Standard deduction (Single) | **$6,350** |
| Free file available | Yes, at https://oktap.tax.ok.gov/ |

## OK Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $1,000 | 0.25% |
| $1,001 - $2,500 | 0.75% |
| $2,501 - $3,750 | 1.75% |
| $3,751 - $4,900 | 2.75% |
| $4,901 - $7,200 | 3.75% |
| Over $7,200 | 4.75% |

**Key insight:** The top rate (4.75%) kicks in at just $7,201 of taxable income. For most W-2 filers, the effective rate is very close to 4.75%.

### Bracket Computation (Single)

```
if ok_taxable <= 1,000:
    ok_tax = ok_taxable * 0.0025
elif ok_taxable <= 2,500:
    ok_tax = 2.50 + (ok_taxable - 1,000) * 0.0075
elif ok_taxable <= 3,750:
    ok_tax = 13.75 + (ok_taxable - 2,500) * 0.0175
elif ok_taxable <= 4,900:
    ok_tax = 35.63 + (ok_taxable - 3,750) * 0.0275
elif ok_taxable <= 7,200:
    ok_tax = 67.25 + (ok_taxable - 4,900) * 0.0375
else:
    ok_tax = 153.50 + (ok_taxable - 7,200) * 0.0475
```

## Calculation

### Step 1: Start from Federal AGI
OK begins with federal AGI (Form 1040, Line 11).

### Step 2: OK Modifications
For W-2-only filers, OK AGI typically equals federal AGI.

### Step 3: OK Standard Deduction
- Single: **$6,350**

### Step 4: OK Taxable Income
```
OK_taxable = OK_AGI - OK_standard_deduction ($6,350)
OK_taxable = max(OK_taxable, 0)
```

### Step 5: Apply Brackets
Use the bracket table above.

### Step 6: Compare to Withholding
```
OK_withheld = W-2 Box 17
OK_refund_or_owed = OK_withheld - OK_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
OK AGI:                $42,829.35
Standard deduction:    -$6,350.00
OK taxable income:     $36,479.35

OK tax calculation:
  0.25% on $1,000:         $2.50
  0.75% on $1,500:        $11.25
  1.75% on $1,250:        $21.88
  2.75% on $1,150:        $31.63
  3.75% on $2,300:        $86.25
  4.75% on $29,279.35: $1,390.77
OK tax:                $1,544.28

OK withheld (Box 17):  $X,XXX.XX
OK refund/owed:        calculated
```

## OK Deductions and Credits

### Standard Deduction
OK offers a $6,350 standard deduction (single, 2025).

### Renter Benefit
OK does **not** offer a general renter's credit or deduction.

### Earned Income Credit
- OK offers its own EIC equal to **5%** of the federal EIC
- If the user qualifies for federal EIC, they also get the OK EIC

### Student Loan Interest
OK does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

## Filing OK State Return

### Form 511
1. Go to https://oktap.tax.ok.gov/
2. Free e-filing available for OK residents
3. Enter federal AGI as starting point
4. Subtract standard deduction ($6,350)
5. Calculate tax from OK brackets
6. Enter withholding from Box 17
7. Calculate refund or amount owed

## What to Tell the User

> "Oklahoma has progressive brackets but the top rate (4.75%) kicks in at just $7,201 of taxable income, so most of your income is effectively taxed at 4.75%. OK offers a $6,350 standard deduction. File for free at oktap.tax.ok.gov."
