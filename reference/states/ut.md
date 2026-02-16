# Utah State Tax Reference

## Overview

Utah has a flat income tax rate with a unique "Taxpayer Tax Credit" mechanism instead of a traditional standard deduction.

| Parameter | Value |
|---|---|
| Tax rate | **4.50%** (flat, applied to all income) |
| Form | TC-40 |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- UT starts from federal AGI |
| Standard deduction | **None** (uses Taxpayer Tax Credit instead) |
| Taxpayer Tax Credit | 6% of (personal exemption + federal standard deduction), phases out |
| Free file available | Yes, at https://tax.utah.gov/ |

## How UT Tax Works

### Starting Point: Federal AGI

Utah begins with federal AGI (Form 1040, Line 11). The 4.50% rate is applied to the full state taxable income.

### The Taxpayer Tax Credit (Unique Mechanism)

Instead of a standard deduction, Utah provides a **nonrefundable tax credit** called the Taxpayer Tax Credit. This credit effectively mimics a deduction but works differently:

1. Start with the sum of: federal standard deduction ($15,750) + personal exemption equivalent ($950 per person, so $950 single)
2. Multiply by **6%** to get the base credit
3. The credit phases out at higher incomes

### Taxpayer Tax Credit Calculation

```
credit_base = (federal_standard_deduction + personal_exemption_amount)
credit_base = $15,750 + $950 = $16,700
base_credit = credit_base * 0.06 = $1,002.00

# Phaseout: credit reduces by 1.3 cents for every dollar of AGI over a threshold
# Threshold is approximately $16,656 (single, 2025)
# For most W-2 filers, the credit will be partially phased out

phaseout_amount = max(0, (state_taxable_income - threshold)) * 0.013
taxpayer_credit = max(0, base_credit - phaseout_amount)
```

**Note:** The exact phaseout formula is complex. For EZFile's target user, the credit typically ranges from $200-$800 depending on income.

### Full Calculation

```
UT_taxable_income = Federal AGI (Form 1040, Line 11)
UT_gross_tax = UT_taxable_income * 0.045
UT_taxpayer_credit = calculated per above
UT_tax = max(UT_gross_tax - UT_taxpayer_credit, 0)
UT_withheld = W-2 Box 17
UT_refund_or_owed = UT_withheld - UT_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
UT taxable income:         $42,829.35
UT gross tax (4.50%):      $1,927.32

Taxpayer Tax Credit:
  Base: ($15,750 + $950) × 6% = $1,002.00
  Phaseout reduction:         ~$339.25
  Net credit:                  ~$662.75

UT net tax:                $1,264.57
UT withheld (Box 17):      $X,XXX.XX
UT refund/owed:            calculated
```

## UT Deductions and Credits

### No Standard Deduction
UT does NOT offer a standard deduction. The Taxpayer Tax Credit serves a similar purpose but works as a credit against tax rather than a deduction from income.

### Renter Benefit (Circuit Breaker)
- Available ONLY to residents age **66 or older**
- NOT applicable to most of EZFile's target users
- Provides property tax/rent relief for low-income seniors

### Earned Income Tax Credit
- UT offers its own EITC equal to **20%** of the federal EIC
- If the user qualifies for federal EIC, they also get the UT EITC

### Student Loan Interest
UT does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

## Filing UT State Return

### TC-40 Form
1. Go to https://tax.utah.gov/
2. Free e-filing available for UT residents
3. Enter federal AGI as starting point
4. Apply 4.50% flat rate to full income
5. Calculate Taxpayer Tax Credit
6. Subtract credit from gross tax
7. Enter withholding from Box 17
8. Calculate refund or amount owed

## What to Tell the User

> "Utah uses a flat 4.50% rate on your federal AGI, then gives you a 'Taxpayer Tax Credit' that works like a deduction-in-disguise. The credit is based on your federal standard deduction and phases out at higher incomes. File for free at tax.utah.gov."
