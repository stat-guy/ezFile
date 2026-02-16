# Idaho State Tax Reference

## Overview

Idaho has a flat income tax that was recently reduced to 5.3% for 2025. Idaho starts from federal taxable income.

| Parameter | Value |
|---|---|
| Tax rate | **5.30%** (flat, 2025; reduced from 5.695% via HB 40) |
| Form | 40 (Form 40) |
| Filing deadline | April 15 |
| Follows federal AGI? | **No** -- ID starts from federal **taxable income** (Line 15) |
| Standard deduction | **None** (uses federal standard deduction indirectly) |
| Free file available | Yes, at https://tax.idaho.gov/ (Idaho Free File + IRS Direct File) |

## How ID Tax Works

### Starting Point: Federal Taxable Income (Line 15)

Idaho starts from **federal taxable income** (Form 1040, Line 15). The federal standard deduction is already subtracted. Idaho then applies Idaho-specific additions and subtractions.

### No Additional Deduction

Because ID starts after the federal standard deduction, there is no ID-specific standard deduction.

### Calculation

```
ID_taxable = Federal taxable income (Form 1040, Line 15)
# Idaho-specific adjustments may apply, minimal for W-2 filers
ID_tax = ID_taxable * 0.053
ID_withheld = W-2 Box 17
ID_refund_or_owed = ID_withheld - ID_tax
```

### Sample Calculation (Federal Taxable Income of $27,079)

```
Federal taxable income (Line 15): $27,079.35
ID tax rate:                       × 5.30%
ID tax owed:                       $1,435.21

ID withheld (Box 17):             $X,XXX.XX
ID refund/owed:                   calculated
```

## ID Deductions and Credits

### No State Standard Deduction
ID starts from federal taxable income, so the federal standard deduction ($15,750) is already applied.

### Grocery Credit
- Idaho offers a **grocery credit** of $120 per person ($40 for dependents under 65)
- Available to all Idaho residents regardless of income
- Refundable credit

### Renter Benefit
ID does **not** offer a renter's credit or deduction.

### Earned Income Credit
- ID does **not** currently offer its own state EIC

### Student Loan Interest
ID does **not** allow a separate student loan interest deduction -- it's already reflected in federal taxable income.

## Filing ID State Return

### Form 40
1. Go to https://tax.idaho.gov/ (Idaho Free File or IRS Direct File)
2. Enter federal taxable income (Form 1040, Line 15) as starting point
3. Apply Idaho-specific adjustments
4. Apply 5.30% flat rate
5. Claim $120 grocery credit
6. Enter withholding from Box 17
7. Calculate refund or amount owed

## What to Tell the User

> "Idaho uses a flat 5.30% rate on your federal taxable income (Line 15, after the standard deduction). You also get a $120 grocery credit. Idaho participates in IRS Direct File for combined free federal/state filing. File for free at tax.idaho.gov."
