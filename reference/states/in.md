# Indiana State Tax Reference

## Overview

Indiana has a low flat state income tax rate, but uniquely also requires county income taxes on top of the state rate.

| Parameter | Value |
|---|---|
| Tax rate | **3.00%** (flat state) + county tax (0.5%–2.95%) |
| Form | IT-40 |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- IN starts from federal AGI |
| Standard deduction | **None** |
| Personal exemption | **$1,000** (single) |
| Free file available | Yes, at https://intime.dor.in.gov/ (INtax) |

## How IN Tax Works

### Starting Point: Federal AGI

Indiana begins with federal AGI (Form 1040, Line 11).

### Personal Exemption

IN does not have a standard deduction. Instead, it offers a flat personal exemption:
- Single: **$1,000**
- This reduces taxable income

### State Tax Calculation

```
IN_AGI = Federal AGI (Form 1040, Line 11)
IN_taxable_income = IN_AGI - personal_exemption ($1,000)
IN_taxable_income = max(IN_taxable_income, 0)
IN_state_tax = IN_taxable_income * 0.03
```

### County Tax (Mandatory)

Indiana is unique in that **every county** levies its own income tax on top of the 3% state rate. This is NOT optional.

| Example Counties | County Rate | Combined Rate |
|---|---|---|
| Marion (Indianapolis) | 2.02% | 5.02% |
| Lake (Gary/Hammond) | 1.50% | 4.50% |
| Allen (Fort Wayne) | 1.48% | 4.48% |
| Hamilton (Carmel) | 1.00% | 4.00% |
| Monroe (Bloomington) | 1.345% | 4.345% |

The county rate is based on the county where the filer **lives** (not works) as of January 1 of the tax year.

### Full Calculation

```
IN_AGI = Federal AGI (Form 1040, Line 11)
IN_taxable_income = IN_AGI - personal_exemption ($1,000)
IN_state_tax = IN_taxable_income * 0.03
IN_county_tax = IN_taxable_income * county_rate
IN_total_tax = IN_state_tax + IN_county_tax
IN_withheld = W-2 Box 17 (may include both state and county)
IN_refund_or_owed = IN_withheld - IN_total_tax
```

### Sample Calculation (Federal AGI of $42,829, Marion County)

```
IN AGI:                $42,829.35
Personal exemption:    -$1,000.00
IN taxable income:     $41,829.35

State tax (3.00%):     $1,254.88
County tax (2.02%):      $844.95
Total IN tax:          $2,099.83

IN withheld (Box 17):  $X,XXX.XX
IN refund/owed:        calculated
```

## IN Deductions and Credits

### No Standard Deduction
IN does NOT offer a standard deduction. Only the $1,000 personal exemption applies.

### Renter's Deduction
- IN allows renters to deduct up to **$4,000** of rent paid
- This is a deduction from income, not a credit
- Must have paid rent on a principal residence in Indiana
- **This applies to EZFile's target user!** Always ask about rent paid.

### Earned Income Credit
- IN offers its own EIC equal to 12% of the federal EIC
- If the user qualifies for federal EIC, they also get the IN EIC

### Student Loan Interest
IN does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

## Filing IN State Return

### IT-40 Form
1. Go to https://intime.dor.in.gov/
2. Free e-filing available for IN residents
3. Enter federal AGI as starting point
4. Subtract personal exemption ($1,000)
5. Subtract renter's deduction if applicable (up to $4,000)
6. Apply 3.00% state rate
7. Look up county tax rate and apply
8. Enter withholding from Box 17
9. Calculate refund or amount owed

### Key Note: County Identification
The W-2 Box 20 (locality) or the filer's address determines which county rate applies. If unclear, ask the user which Indiana county they lived in on January 1, 2025.

## What to Tell the User

> "Indiana has a flat 3.00% state income tax, but your county also charges its own income tax on top of that (rates vary from 0.5% to nearly 3%). Your total IN rate is about [X]%. Good news for renters: Indiana lets you deduct up to $4,000 of rent paid. File for free at intime.dor.in.gov."
