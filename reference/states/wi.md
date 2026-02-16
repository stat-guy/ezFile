# Wisconsin State Tax Reference

## Overview

Wisconsin has a progressive income tax with 4 brackets and a sliding-scale standard deduction that phases out at higher incomes.

| Parameter | Value |
|---|---|
| Tax type | Progressive (4 brackets) |
| Form | 1 (Form 1) |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- WI starts from federal AGI |
| Standard deduction (Single) | Up to **$14,260** (sliding scale, phases out) |
| Free file available | Yes, at https://www.revenue.wi.gov/ (WI E-File) |

## WI Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $14,320 | 3.50% |
| $14,321 - $28,640 | 4.40% |
| $28,641 - $315,310 | 5.30% |
| Over $315,310 | 7.65% |

**For EZFile's target user:** The first 3 brackets (up to $315,310) are most relevant.

### Bracket Computation (Single)

```
if wi_taxable <= 14,320:
    wi_tax = wi_taxable * 0.035
elif wi_taxable <= 28,640:
    wi_tax = 501.20 + (wi_taxable - 14,320) * 0.044
elif wi_taxable <= 315,310:
    wi_tax = 1,131.28 + (wi_taxable - 28,640) * 0.053
else:
    wi_tax = 16,324.78 + (wi_taxable - 315,310) * 0.0765
```

## How WI Tax Works

### Step 1: Start from Federal AGI
WI begins with federal AGI (Form 1040, Line 11).

### Step 2: WI Modifications
For W-2-only filers, WI AGI typically equals federal AGI. WI has some additions/subtractions but they rarely apply to simple W-2 filers.

### Step 3: WI Standard Deduction (Sliding Scale)

Wisconsin's standard deduction is unique -- it starts at a maximum and **phases out** as income increases:

| WI AGI (Single) | Standard Deduction |
|---|---|
| $0 - $16,630 | $14,260 (maximum) |
| $16,631 - $93,200 | Reduces by 12% of AGI over $16,630 |
| Above ~$135,500 | $0 (fully phased out) |

**Formula:**
```
if WI_AGI <= 16,630:
    WI_std_ded = 14,260
elif WI_AGI <= 93,200:
    reduction = (WI_AGI - 16,630) * 0.12
    WI_std_ded = max(14,260 - reduction, 0)
else:
    WI_std_ded = 0
```

**Example at $42,829 AGI:**
```
reduction = ($42,829 - $16,630) × 12% = $26,199 × 0.12 = $3,143.88
WI_std_ded = $14,260 - $3,143.88 = $11,116.12
```

### Step 4: WI Taxable Income
```
WI_taxable = WI_AGI - WI_standard_deduction
WI_taxable = max(WI_taxable, 0)
```

### Step 5: Apply Brackets
Use the bracket table above.

### Step 6: Compare to Withholding
```
WI_withheld = W-2 Box 17
WI_refund_or_owed = WI_withheld - WI_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
WI AGI:                $42,829.35
Standard deduction:   -$11,116.12 (reduced from $14,260 max)
WI taxable income:     $31,713.23

WI tax calculation:
  3.50% on $14,320:       $501.20
  4.40% on $14,320:       $630.08
  5.30% on $3,073.23:     $162.88
WI gross tax:            $1,294.16

WI withheld (Box 17):   $X,XXX.XX
WI refund/owed:         calculated
```

## WI Deductions and Credits

### Sliding-Scale Standard Deduction
WI's standard deduction phases out as income increases (see above). This effectively raises the marginal tax rate for middle-income filers.

### Homestead Credit (Renters!)
- Available to WI renters AND homeowners with **household income under $24,680**
- Credit is based on property taxes or **25% of rent paid** (treated as property tax)
- Maximum credit: **$1,168** (2025 estimated)
- **This may apply to lower-income EZFile users!** Check income threshold.

### Earned Income Credit
- WI offers its own EIC equal to **4%** of the federal EIC (no children)
- If the user qualifies for federal EIC, they also get the WI EIC
- WI's rate for no-children filers is relatively small

### Student Loan Interest
WI does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

### Itemized Deduction Credit
WI allows a credit for certain itemized deductions even for standard deduction filers. For W-2-only filers this is rarely applicable.

## Filing WI State Return

### Form 1
1. Go to https://www.revenue.wi.gov/ (WI E-File)
2. Free e-filing available for WI residents
3. Enter federal AGI as starting point
4. Calculate sliding-scale standard deduction
5. Calculate tax from WI brackets
6. Check Homestead Credit eligibility (income under $24,680)
7. Enter withholding from Box 17
8. Calculate refund or amount owed

## What to Tell the User

> "Wisconsin has progressive brackets (3.5%-7.65%) and a standard deduction that shrinks as your income rises. At your income level, your WI standard deduction is about $[X] (reduced from the $14,260 maximum). If your household income is under $24,680, you may also qualify for the Homestead Credit -- WI treats 25% of your rent as property tax for this credit. File for free at revenue.wi.gov."
