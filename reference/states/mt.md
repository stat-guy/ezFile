# Montana State Tax Reference

## Overview

Montana reformed its tax system in 2024, collapsing from seven brackets to two. Montana has no sales tax.

| Parameter | Value |
|---|---|
| Tax type | Progressive (2 brackets) |
| Form | 2 (Form 2) |
| Filing deadline | April 15 |
| Follows federal AGI? | **No** -- MT starts from federal **taxable income** (Line 15) |
| Standard deduction | **None** (uses federal standard deduction indirectly) |
| Free file available | Yes, via Free File Alliance at https://revenue.mt.gov/ |

## MT Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $21,100 | 4.70% |
| Over $21,100 | 5.90% |

### Bracket Computation (Single)

```
if mt_taxable <= 21,100:
    mt_tax = mt_taxable * 0.047
else:
    mt_tax = 991.70 + (mt_taxable - 21,100) * 0.059
```

## How MT Tax Works

### Starting Point: Federal Taxable Income (Line 15)

Montana starts from **federal taxable income** (Form 1040, Line 15). The federal standard deduction is already subtracted before Montana applies its brackets.

### No Additional Deduction

Because MT starts after the federal standard deduction, there is no MT-specific standard deduction.

### Calculation

```
MT_taxable = Federal taxable income (Form 1040, Line 15)
# MT-specific adjustments may apply
MT_tax = apply brackets to MT_taxable
MT_withheld = W-2 Box 17
MT_refund_or_owed = MT_withheld - MT_tax
```

### Sample Calculation (Federal Taxable Income of $27,079)

```
Federal taxable income (Line 15): $27,079.35

MT tax calculation:
  4.70% on $21,100:       $991.70
  5.90% on $5,979.35:     $352.78
MT tax:                  $1,344.48

MT withheld (Box 17):    $X,XXX.XX
MT refund/owed:          calculated
```

## MT Deductions and Credits

### No State Standard Deduction
MT starts from federal taxable income, so the federal standard deduction ($15,750) is already applied.

### No Sales Tax
Montana has no sales tax, similar to Oregon and Delaware.

### Renter Benefit
MT does **not** offer a general renter's credit or deduction. A property tax credit exists for **62+ or disabled** only.

### Earned Income Credit
- MT offers its own EIC equal to **3%** of the federal EIC
- If the user qualifies for federal EIC, they also get the MT EIC

### 65+ Subtraction
Taxpayers age 65+ receive a **$5,500** subtraction from federal taxable income.

### Student Loan Interest
MT does **not** allow a separate student loan interest deduction -- it's already reflected in federal taxable income.

## Filing MT State Return

### Form 2
1. Go to https://revenue.mt.gov/ (Free File Alliance)
2. Enter federal taxable income (Form 1040, Line 15) as starting point
3. Apply MT adjustments
4. Calculate tax from MT brackets
5. Enter withholding from Box 17
6. Calculate refund or amount owed

## What to Tell the User

> "Montana has two tax brackets (4.70% and 5.90%) starting from your federal taxable income (Line 15). Like Oregon and Delaware, Montana has no sales tax. File via Free File Alliance at revenue.mt.gov."
