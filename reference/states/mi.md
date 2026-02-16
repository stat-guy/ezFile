# Michigan State Tax Reference

## Overview

Michigan has a simple flat income tax rate with a generous personal exemption and a valuable Homestead Property Tax Credit for renters.

| Parameter | Value |
|---|---|
| Tax rate | **4.25%** (flat) |
| Form | MI-1040 |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- MI starts from federal AGI |
| Standard deduction | **None** |
| Personal exemption | **$5,600** (single, 2025 estimated, indexed) |
| Free file available | Yes, at https://www.michigan.gov/taxes |

## How MI Tax Works

### Starting Point: Federal AGI

Michigan begins with federal AGI (Form 1040, Line 11).

### Personal Exemption

MI does not have a standard deduction. Instead, it offers a personal exemption:
- Single: **$5,600** (2025 estimated, indexed for inflation)
- This reduces taxable income

### Calculation

```
MI_AGI = Federal AGI (Form 1040, Line 11)
MI_taxable_income = MI_AGI - personal_exemption ($5,600)
MI_taxable_income = max(MI_taxable_income, 0)
MI_tax = MI_taxable_income * 0.0425
MI_withheld = W-2 Box 17
MI_refund_or_owed = MI_withheld - MI_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
MI AGI:                $42,829.35
Personal exemption:    -$5,600.00
MI taxable income:     $37,229.35

MI tax rate:           × 4.25%
MI tax owed:           $1,582.25

MI withheld (Box 17):  $X,XXX.XX
MI refund/owed:        calculated
```

## MI Deductions and Credits

### No Standard Deduction
MI does NOT offer a standard deduction. Only the personal exemption ($5,600) applies.

### Homestead Property Tax Credit (Renters!)
- Available to MI renters AND homeowners with **household income ≤ $63,000** (approximately)
- For renters: **20% of rent paid** is treated as property tax
- Credit = property taxes (or 20% of rent) minus 3.5% of household income
- Maximum credit: **$1,700**
- **This applies to EZFile's target user!** Always ask about rent paid and household income.

**Example:**
```
Annual rent: $12,000
Property tax equivalent: $12,000 × 20% = $2,400
3.5% of household income ($42,829): $1,499.02
Credit = $2,400 - $1,499.02 = $900.98
```

### Earned Income Credit
- MI offers its own EIC equal to **30%** of the federal EIC
- If the user qualifies for federal EIC, they also get the MI EIC

### Student Loan Interest
MI does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

### City Income Tax
Some MI cities levy their own income tax (Detroit: 2.4%, others: ~1%). Check W-2 Box 18-20 for local withholding.

## Filing MI State Return

### MI-1040 Form
1. Go to https://www.michigan.gov/taxes
2. Free e-filing available for MI residents
3. Enter federal AGI as starting point
4. Subtract personal exemption ($5,600)
5. Apply 4.25% flat rate
6. Check Homestead Property Tax Credit eligibility
7. Enter withholding from Box 17
8. Calculate refund or amount owed

## What to Tell the User

> "Michigan uses a flat 4.25% rate on your federal AGI minus a $5,600 personal exemption. Great news for renters: Michigan's Homestead Property Tax Credit treats 20% of your rent as property tax and gives you a credit if that exceeds 3.5% of your income (max $1,700). File for free at michigan.gov/taxes."
