# Mississippi State Tax Reference

## Overview

Mississippi has a flat income tax rate with the first $10,000 of taxable income exempt. Mississippi is phasing out its income tax entirely, with rates declining each year through 2030.

| Parameter | Value |
|---|---|
| Tax rate | **4.4%** (flat, on income over $10,000; 2025) |
| Form | 80-105 |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- MS starts from federal AGI |
| Standard deduction (Single) | **$2,300** |
| Personal exemption | **$6,000** (single) |
| Free file available | Yes, via approved e-file providers at https://www.dor.ms.gov/ |

## How MS Tax Works

### Starting Point: Federal AGI

Mississippi begins with federal AGI (Form 1040, Line 11), then applies Mississippi-specific adjustments.

### Standard Deduction + Personal Exemption

MS provides both:
- Standard deduction (Single): **$2,300**
- Personal exemption (Single): **$6,000**
- Total deductions from income: $2,300 + $6,000 = **$8,300**

### Tax-Free Threshold

After deductions, the first **$10,000** of taxable income is exempt (0% rate). Only income above $10,000 is taxed at 4.4%.

### Calculation

```
MS_AGI = Federal AGI (Form 1040, Line 11)
MS_taxable_income = MS_AGI - MS_std_deduction ($2,300) - MS_personal_exemption ($6,000)
MS_taxable_income = max(MS_taxable_income, 0)

# First $10,000 is exempt
MS_taxable_above_threshold = max(MS_taxable_income - 10,000, 0)
MS_tax = MS_taxable_above_threshold * 0.044
MS_withheld = W-2 Box 17
MS_refund_or_owed = MS_withheld - MS_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
MS AGI:                    $42,829.35
Standard deduction:        -$2,300.00
Personal exemption:        -$6,000.00
MS taxable income:         $34,529.35

First $10,000 exempt:     -$10,000.00
MS taxable above threshold: $24,529.35

MS tax rate:               × 4.4%
MS tax owed:               $1,079.29

MS withheld (Box 17):     $X,XXX.XX
MS refund/owed:           calculated
```

## Income Tax Phase-Out Schedule

Mississippi is eliminating its income tax:

| Tax Year | Rate | Exempt Amount |
|---|---|---|
| 2024 | 4.7% | $10,000 |
| 2025 | 4.4% | $10,000 |
| 2026 | 4.0% | $10,000 |
| 2027 | 3.75% | $10,000 |
| 2028 | 3.50% | $10,000 |
| 2029 | 3.25% | $10,000 |
| 2030 | 3.0% | $10,000 |
| 2031+ | Trigger-based further reductions toward 0% |

## MS Deductions and Credits

### Standard Deduction + Personal Exemption
MS provides a combined $8,300 in deductions ($2,300 standard + $6,000 personal exemption), plus the $10,000 exempt threshold. Effectively, the first ~$18,300 of income is tax-free.

### Renter Benefit
MS does **not** offer a renter's credit or deduction.

### Earned Income Credit
- MS does **not** currently offer its own state EIC

### Student Loan Interest
MS does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

## Filing MS State Return

### Form 80-105
1. Go to https://www.dor.ms.gov/
2. File through approved e-file providers
3. Enter federal AGI as starting point
4. Subtract standard deduction ($2,300) and personal exemption ($6,000)
5. Subtract $10,000 exempt threshold
6. Apply 4.4% rate on remaining income
7. Enter withholding from Box 17
8. Calculate refund or amount owed

## What to Tell the User

> "Mississippi taxes income at 4.4%, but with generous exemptions: a $2,300 standard deduction, $6,000 personal exemption, and the first $10,000 of taxable income is completely exempt. So effectively your first ~$18,300 of income is tax-free. Good news: Mississippi is phasing out its income tax entirely -- the rate drops each year through 2030. File through approved e-file providers at dor.ms.gov."
