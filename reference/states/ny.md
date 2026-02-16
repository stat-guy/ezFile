# New York State Tax Reference

## Overview

New York has a progressive income tax with multiple brackets. NYC residents also pay an additional city income tax.

| Parameter | Value |
|---|---|
| Tax type | Progressive (graduated brackets) |
| Form | IT-201 (resident) |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- NY starts from federal AGI |
| Standard deduction (Single) | **$8,000** |
| Free file available | Yes, at https://www.tax.ny.gov/ |

## NY Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $8,500 | 4.00% |
| $8,501 - $11,700 | 4.50% |
| $11,701 - $13,900 | 5.25% |
| $13,901 - $80,650 | 5.50% |
| $80,651 - $215,400 | 6.00% |
| $215,401 - $1,077,550 | 6.85% |
| $1,077,551 - $5,000,000 | 9.65% |
| Over $5,000,000 | 10.90% |

**For EZFile's target user:** The first 4 brackets (up to $80,650) are most relevant.

### Bracket Computation (Single)

```
if ny_taxable <= 8,500:
    ny_tax = ny_taxable * 0.04
elif ny_taxable <= 11,700:
    ny_tax = 340 + (ny_taxable - 8,500) * 0.045
elif ny_taxable <= 13,900:
    ny_tax = 484 + (ny_taxable - 11,700) * 0.0525
elif ny_taxable <= 80,650:
    ny_tax = 600 + (ny_taxable - 13,900) * 0.055
elif ny_taxable <= 215,400:
    ny_tax = 4,271 + (ny_taxable - 80,650) * 0.06
else:
    # Higher brackets exist but unlikely for this profile
    ny_tax = 12,356 + (ny_taxable - 215,400) * 0.0685
```

## Calculation

### Step 1: Start from Federal AGI
NY begins with the federal AGI (Form 1040, Line 11).

### Step 2: NY Additions and Subtractions
For this profile, typically no additions or subtractions needed.
- NY does NOT allow the student loan interest deduction separately (it's already in federal AGI)
- No NY-specific additions for W-2-only filers

### Step 3: NY AGI
Usually equals federal AGI for this profile.

### Step 4: NY Standard Deduction
- Single: **$8,000** (2025)
- This is lower than the federal standard deduction

### Step 5: NY Taxable Income
```
NY_taxable = NY_AGI - NY_standard_deduction
NY_taxable = max(NY_taxable, 0)
```

### Step 6: Apply Brackets
Use the bracket table above.

### Step 7: Compare to Withholding
```
NY_withheld = W-2 Box 17
NY_refund_or_owed = NY_withheld - NY_tax
```

## NYC Income Tax (If NYC Resident)

NYC residents pay an additional city income tax on top of the state tax.

### NYC Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $12,000 | 3.078% |
| $12,001 - $25,000 | 3.762% |
| $25,001 - $50,000 | 3.819% |
| Over $50,000 | 3.876% |

### NYC Handling
- NYC tax is filed on the same IT-201 form
- Check if the user lives in one of the 5 boroughs (Manhattan, Brooklyn, Queens, Bronx, Staten Island)
- W-2 may show NYC withholding separately or combined with state

### Yonkers Tax
Yonkers residents pay a surcharge equal to a percentage of their NY state tax:
- Resident: 16.75% of NY state tax
- Nonresident working in Yonkers: 0.5% of wages

## Sample Calculation (Federal AGI of $42,829)

```
NY AGI:                $42,829.35
NY standard deduction: -$8,000.00
NY taxable income:     $34,829.35

NY tax calculation:
  4.00% on $8,500:        $340.00
  4.50% on $3,200:        $144.00
  5.25% on $2,200:        $115.50
  5.50% on $20,929.35:  $1,151.11
NY state tax:           $1,750.61

NY withheld (Box 17):  $X,XXX.XX
NY refund/owed:        calculated
```

## Key NY-Specific Items

### STAR Credit
- For homeowners only -- NOT applicable to EZFile's target user (renters)

### NYC School Tax Credit
- Available to NYC residents with income under $250,000
- Fixed amount: $63 (single filer)
- Refundable credit

### NY Earned Income Credit
- NY has its own EIC equal to 30% of the federal EIC
- If the user qualifies for federal EIC, they also get the NY EIC

## Filing NY State Return

### IT-201 Form
1. Go to https://www.tax.ny.gov/
2. Select e-file options
3. Enter federal AGI as starting point
4. Apply NY standard deduction ($8,000)
5. Calculate tax from brackets
6. Enter withholding from Box 17
7. Calculate refund or amount owed

## What to Tell the User

> "New York starts from your federal AGI and applies its own tax brackets. NY's standard deduction ($8,000) is lower than the federal one ($15,750), so your NY taxable income will be higher than your federal taxable income. [If NYC:] As a New York City resident, you also pay a separate city income tax on top of the state tax."
