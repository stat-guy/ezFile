# Hawaii State Tax Reference

## Overview

Hawaii has the most tax brackets of any state (12!) and some of the highest rates, but lower-income filers benefit from low starting rates and a low-income renter's credit.

| Parameter | Value |
|---|---|
| Tax type | Progressive (12 brackets) |
| Form | N-11 (resident) |
| Filing deadline | April 20 (Hawaii's deadline is later than most states!) |
| Follows federal AGI? | **Yes** -- HI starts from federal AGI |
| Standard deduction (Single) | **$2,200** (very low) |
| Personal exemption | **$1,144** |
| Free file available | Yes, at https://tax.hawaii.gov/ (Hawaii Tax Online) |

## HI Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $2,400 | 1.40% |
| $2,401 - $4,800 | 3.20% |
| $4,801 - $9,600 | 5.50% |
| $9,601 - $14,400 | 6.40% |
| $14,401 - $19,200 | 6.80% |
| $19,201 - $24,000 | 7.20% |
| $24,001 - $36,000 | 7.60% |
| $36,001 - $48,000 | 7.90% |
| $48,001 - $150,000 | 8.25% |
| $150,001 - $175,000 | 9.00% |
| $175,001 - $200,000 | 10.00% |
| Over $200,000 | 11.00% |

**For EZFile's target user:** The first 9 brackets (up to $150,000) are most relevant.

### Bracket Computation (Single)

```
if hi_taxable <= 2,400:
    hi_tax = hi_taxable * 0.014
elif hi_taxable <= 4,800:
    hi_tax = 33.60 + (hi_taxable - 2,400) * 0.032
elif hi_taxable <= 9,600:
    hi_tax = 110.40 + (hi_taxable - 4,800) * 0.055
elif hi_taxable <= 14,400:
    hi_tax = 374.40 + (hi_taxable - 9,600) * 0.064
elif hi_taxable <= 19,200:
    hi_tax = 681.60 + (hi_taxable - 14,400) * 0.068
elif hi_taxable <= 24,000:
    hi_tax = 1,008.00 + (hi_taxable - 19,200) * 0.072
elif hi_taxable <= 36,000:
    hi_tax = 1,353.60 + (hi_taxable - 24,000) * 0.076
elif hi_taxable <= 48,000:
    hi_tax = 2,265.60 + (hi_taxable - 36,000) * 0.079
elif hi_taxable <= 150,000:
    hi_tax = 3,213.60 + (hi_taxable - 48,000) * 0.0825
else:
    # Higher brackets exist but unlikely for this profile
    hi_tax = 11,628.60 + (hi_taxable - 150,000) * 0.09
```

## Calculation

### Step 1: Start from Federal AGI
HI begins with federal AGI (Form 1040, Line 11).

### Step 2: HI Modifications
For W-2-only filers, HI AGI typically equals federal AGI. Hawaii generally conforms to federal definitions for wage income.

### Step 3: HI Standard Deduction + Personal Exemption
- Standard deduction (Single): **$2,200** (one of the lowest in the country)
- Personal exemption: **$1,144**
- Total deductions from income: $2,200 + $1,144 = **$3,344**

### Step 4: HI Taxable Income
```
HI_taxable = HI_AGI - HI_standard_deduction ($2,200) - HI_personal_exemption ($1,144)
HI_taxable = max(HI_taxable, 0)
```

### Step 5: Apply Brackets
Use the bracket table above.

### Step 6: Compare to Withholding
```
HI_withheld = W-2 Box 17
HI_refund_or_owed = HI_withheld - HI_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
HI AGI:                $42,829.35
Standard deduction:    -$2,200.00
Personal exemption:    -$1,144.00
HI taxable income:     $39,485.35

HI tax calculation:
  1.40% on $2,400:          $33.60
  3.20% on $2,400:          $76.80
  5.50% on $4,800:         $264.00
  6.40% on $4,800:         $307.20
  6.80% on $4,800:         $326.40
  7.20% on $4,800:         $345.60
  7.60% on $12,000:        $912.00
  7.90% on $3,485.35:      $275.34
HI tax:                  $2,540.94

HI withheld (Box 17):   $X,XXX.XX
HI refund/owed:         calculated
```

## HI Deductions and Credits

### Standard Deduction
HI's standard deduction ($2,200 single) is one of the lowest in the country, meaning HI taxes a much larger portion of income compared to states with higher deductions.

### Low-Income Renter's Credit
- Available to HI renters with **AGI under $30,000** (single, approximately)
- Credit amount: **$50** (single)
- Must have paid rent for at least 9 months in HI
- **Check for lower-income EZFile users**

### Food/Excise Tax Credit
- Refundable credit for lower-income filers
- $110 per person (single) if federal AGI ≤ $30,000

### Earned Income Credit
- HI does **not** currently offer its own state EIC

### Student Loan Interest
HI does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

## Filing HI State Return

### Form N-11
1. Go to https://tax.hawaii.gov/ (Hawaii Tax Online)
2. Free e-filing available for HI residents
3. **Note: HI deadline is April 20** (not April 15!)
4. Enter federal AGI as starting point
5. Subtract standard deduction ($2,200) and personal exemption ($1,144)
6. Calculate tax from HI's 12 brackets
7. Check low-income renter's credit and food/excise credit
8. Enter withholding from Box 17
9. Calculate refund or amount owed

## What to Tell the User

> "Hawaii has 12 tax brackets (the most of any state), ranging from 1.4% to 11%. The standard deduction is very low ($2,200), so your HI taxable income will be significantly higher than your federal amount. Important: Hawaii's filing deadline is **April 20**. File for free at tax.hawaii.gov."
