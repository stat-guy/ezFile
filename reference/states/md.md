# Maryland State Tax Reference

## Overview

Maryland has a progressive income tax with 8 brackets AND mandatory county income taxes on top of state tax (similar to Indiana).

| Parameter | Value |
|---|---|
| Tax type | Progressive (8 brackets) + county tax |
| Form | 502 (resident) |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- MD starts from federal AGI |
| Standard deduction (Single) | **15% of MD AGI** (min $1,800, max $2,550) |
| Free file available | Yes, at https://www.marylandtaxes.gov/ |

## MD State Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $1,000 | 2.00% |
| $1,001 - $2,000 | 3.00% |
| $2,001 - $3,000 | 4.00% |
| $3,001 - $100,000 | 4.75% |
| $100,001 - $125,000 | 5.00% |
| $125,001 - $150,000 | 5.25% |
| $150,001 - $250,000 | 5.50% |
| Over $250,000 | 5.75% |

**For EZFile's target user:** The first 4 brackets (up to $100,000) are most relevant. Practically, most income falls in the 4.75% bracket.

### Bracket Computation (Single)

```
if md_taxable <= 1,000:
    md_tax = md_taxable * 0.02
elif md_taxable <= 2,000:
    md_tax = 20 + (md_taxable - 1,000) * 0.03
elif md_taxable <= 3,000:
    md_tax = 50 + (md_taxable - 2,000) * 0.04
elif md_taxable <= 100,000:
    md_tax = 90 + (md_taxable - 3,000) * 0.0475
elif md_taxable <= 125,000:
    md_tax = 4,697.50 + (md_taxable - 100,000) * 0.05
elif md_taxable <= 150,000:
    md_tax = 5,947.50 + (md_taxable - 125,000) * 0.0525
elif md_taxable <= 250,000:
    md_tax = 7,260.00 + (md_taxable - 150,000) * 0.055
else:
    md_tax = 12,760.00 + (md_taxable - 250,000) * 0.0575
```

## County Tax (Mandatory)

Maryland requires **every resident** to pay a county income tax on top of the state tax. Rates vary by county:

| Example Counties | County Rate |
|---|---|
| Montgomery County | 3.20% |
| Baltimore County | 3.20% |
| Baltimore City | 3.20% |
| Prince George's County | 3.20% |
| Howard County | 3.20% |
| Anne Arundel County | 2.81% |
| Frederick County | 2.96% |
| Worcester County | 2.25% (lowest) |

Most MD counties charge **3.20%** (the maximum). The county tax is calculated on MD taxable income.

## Calculation

### Step 1: Start from Federal AGI
MD begins with federal AGI (Form 1040, Line 11).

### Step 2: MD Standard Deduction (Percentage-Based)
MD's standard deduction is unique -- it's **15% of MD AGI** with a floor and cap:
- Minimum: **$1,800**
- Maximum: **$2,550** (single)

```
MD_std_ded = MD_AGI * 0.15
MD_std_ded = max(MD_std_ded, 1,800)
MD_std_ded = min(MD_std_ded, 2,550)
```

For most W-2 filers with AGI above ~$17,000, the deduction will be capped at $2,550.

### Step 3: MD Taxable Income
```
MD_taxable = MD_AGI - MD_standard_deduction
MD_taxable = max(MD_taxable, 0)
```

### Step 4: Apply State Brackets + County Rate
```
MD_state_tax = apply brackets to MD_taxable
MD_county_tax = MD_taxable * county_rate
MD_total_tax = MD_state_tax + MD_county_tax
```

### Step 5: Compare to Withholding
```
MD_withheld = W-2 Box 17 (typically includes both state and county)
MD_refund_or_owed = MD_withheld - MD_total_tax
```

### Sample Calculation (Federal AGI of $42,829, Montgomery County)

```
MD AGI:                    $42,829.35
Standard deduction:        -$2,550.00 (capped; 15% × $42,829 = $6,424 > $2,550)
MD taxable income:         $40,279.35

MD state tax:
  2.00% on $1,000:            $20.00
  3.00% on $1,000:            $30.00
  4.00% on $1,000:            $40.00
  4.75% on $37,279.35:     $1,770.77
MD state tax:              $1,860.77

County tax (Montgomery 3.20%):
  3.20% × $40,279.35:      $1,288.94

Total MD tax:              $3,149.71

MD withheld (Box 17):      $X,XXX.XX
MD refund/owed:            calculated
```

## MD Deductions and Credits

### Standard Deduction (Percentage-Based)
MD's standard deduction is very small (15% of AGI, capped at $2,550 single). This is one of the lowest effective standard deductions in the country.

### Renter's Tax Credit
- Available to qualifying MD renters
- Must apply to the Maryland Department of Assessments and Taxation
- Income limits apply (generally household income ≤ $60,000)
- Credit can be significant (based on rent vs. income ratio)
- **Application required** -- not automatic on the tax return
- **Mention this to EZFile users who rent in MD**

### Earned Income Credit
- MD offers both a refundable EIC (28% of federal) and a nonrefundable EIC (50% of federal)
- If the user qualifies for federal EIC, they can choose the more beneficial MD EIC

### Student Loan Interest
MD does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

### Poverty Level Credit
Low-income filers may qualify for a credit that reduces or eliminates MD tax.

## Filing MD State Return

### Form 502
1. Go to https://www.marylandtaxes.gov/
2. Free e-filing available for MD residents
3. Enter federal AGI as starting point
4. Calculate standard deduction (15% of AGI, min $1,800, max $2,550)
5. Calculate state tax from brackets
6. Look up county tax rate and apply
7. Check Renter's Tax Credit eligibility (separate application)
8. Enter withholding from Box 17
9. Calculate refund or amount owed

### Key Note: County Identification
The filer's county is determined by their residence address. If unclear, ask the user which Maryland county they live in.

## What to Tell the User

> "Maryland has progressive brackets (2%-5.75%) plus a mandatory county income tax (typically 3.20%). MD's standard deduction is small -- only 15% of your AGI, capped at $2,550. Your combined state+county rate is effectively about 8% on most income. Renters: MD offers a Renter's Tax Credit (separate application at dat.maryland.gov). File for free at marylandtaxes.gov."
