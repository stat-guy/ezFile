# Massachusetts State Tax Reference

## Overview

Massachusetts has a flat income tax rate but uses its own income definition -- it does NOT simply start from federal AGI.

| Parameter | Value |
|---|---|
| Tax rate | **5.00%** (flat) |
| Form | 1 (Form 1) |
| Filing deadline | April 15 |
| Follows federal AGI? | **No** -- MA uses its own gross income definition |
| Standard deduction | **None** |
| Personal exemption | **$4,400** (single) |
| Free file available | Yes, at https://www.mass.gov/masstaxconnect |

## How MA Tax Works

### Starting Point: MA Gross Income (Not Federal AGI)

Massachusetts does NOT start from federal AGI. It has its own definition of gross income (called "Massachusetts gross income" or "5.0% income"). However, for most W-2-only filers, the key differences are minimal:

- MA starts from wages (similar to W-2 Box 1 or Box 16)
- MA may add back certain items that the federal return excludes
- For simple W-2 filers, MA gross income is usually close to federal gross income

**For EZFile's target user (W-2 only):** Use W-2 Box 16 (state wages) if available. If Box 16 is blank, use Box 1 (federal wages).

### Personal Exemption

MA does not have a standard deduction. Instead, it offers a personal exemption:
- Single: **$4,400**
- This reduces taxable income

### Calculation

```
MA_gross_income = W-2 Box 16 (or Box 1 if Box 16 is blank)
MA_taxable_income = MA_gross_income - personal_exemption ($4,400)
MA_taxable_income = max(MA_taxable_income, 0)
MA_tax = MA_taxable_income * 0.05
MA_withheld = W-2 Box 17
MA_refund_or_owed = MA_withheld - MA_tax
```

### Sample Calculation (MA Wages of $44,629)

```
MA gross income:       $44,629.35
Personal exemption:    -$4,400.00
MA taxable income:     $40,229.35

MA tax rate:           × 5.00%
MA tax owed:           $2,011.47

MA withheld (Box 17):  $X,XXX.XX
MA refund/owed:        calculated
```

## MA Deductions and Credits

### No Standard Deduction
MA does NOT offer a standard deduction. Only the $4,400 personal exemption applies.

### Rent Deduction
- MA allows a deduction of **50% of rent paid**, up to **$4,000**
- This is a deduction from income, not a credit
- Must be for rent on a principal residence in Massachusetts
- **This applies to EZFile's target user!** Always ask about rent paid.

### Commuter Deduction
- MA allows a deduction for commuter costs (transit passes, parking)
- Not common enough to prompt for in EZFile

### Earned Income Credit
- MA offers its own EIC equal to **40%** of the federal EIC
- If the user qualifies for federal EIC, they also get the MA EIC
- One of the most generous state EICs

### Student Loan Interest
MA allows a deduction for student loan interest paid, up to **$2,500** -- similar to the federal deduction.

### No-Tax Status
- If MA AGI is at or below $8,000 (single), no MA tax is owed
- Unlikely for most W-2 filers but check for part-year/low-wage workers

## Filing MA State Return

### Form 1
1. Go to https://www.mass.gov/masstaxconnect
2. Free e-filing available for MA residents
3. Enter MA gross income (Box 16 or Box 1)
4. Subtract personal exemption ($4,400)
5. Subtract rent deduction if applicable (50% of rent, up to $4,000)
6. Apply 5.00% flat rate
7. Enter withholding from Box 17
8. Calculate refund or amount owed

## What to Tell the User

> "Massachusetts uses a flat 5.00% tax rate with a $4,400 personal exemption instead of a standard deduction. Good news for renters: MA lets you deduct 50% of your rent paid, up to $4,000. File for free at mass.gov/masstaxconnect."
