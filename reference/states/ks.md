# Kansas State Tax Reference

## Overview

Kansas recently consolidated from three brackets to two (via SB 1, 2024) and offers a large personal exemption.

| Parameter | Value |
|---|---|
| Tax type | Progressive (2 brackets) |
| Form | K-40 |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- KS starts from federal AGI |
| Standard deduction (Single) | **$3,605** |
| Personal exemption | **$9,160** (single/HoH/MFS) |
| Free file available | Yes, at https://www.kansas.gov/webfile/ (Kansas WebFile + IRS Direct File) |

## KS Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $23,000 | 5.20% |
| Over $23,000 | 5.58% |

### Bracket Computation (Single)

```
if ks_taxable <= 23,000:
    ks_tax = ks_taxable * 0.052
else:
    ks_tax = 1,196 + (ks_taxable - 23,000) * 0.0558
```

## Calculation

### Step 1: Start from Federal AGI
KS begins with federal AGI (Form 1040, Line 11), then applies Kansas-specific modifications via Schedule S.

### Step 2: KS Standard Deduction + Personal Exemption
- Standard deduction (Single): **$3,605**
- Personal exemption (Single): **$9,160** (plus $2,320 per dependent)
- Total deductions from income: $3,605 + $9,160 = **$12,765**

### Step 3: KS Taxable Income
```
KS_taxable = KS_AGI - KS_standard_deduction ($3,605) - KS_personal_exemption ($9,160)
KS_taxable = max(KS_taxable, 0)
```

### Step 4: Apply Brackets

### Step 5: Compare to Withholding

### Sample Calculation (Federal AGI of $42,829)

```
KS AGI:                $42,829.35
Standard deduction:    -$3,605.00
Personal exemption:    -$9,160.00
KS taxable income:     $30,064.35

KS tax calculation:
  5.20% on $23,000:     $1,196.00
  5.58% on $7,064.35:     $394.19
KS tax:                $1,590.19

KS withheld (Box 17):  $X,XXX.XX
KS refund/owed:        calculated
```

## KS Deductions and Credits

### Standard Deduction + Personal Exemption
KS provides both. The combined $12,765 in deductions is relatively generous.

### Homestead Refund (Renters!)
- Available to KS renters who are **55 or older, disabled, or have a dependent child under 18**
- Also available to all renters with **household income ≤ $37,750** (approximately)
- For renters: **15% of rent paid** is treated as property tax
- Filed on Form K-40H
- **May apply to lower-income EZFile users**

### Earned Income Credit
- KS does **not** currently offer its own state EIC

### Student Loan Interest
KS does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

## Filing KS State Return

### Form K-40
1. Go to https://www.kansas.gov/webfile/ (Kansas WebFile -- free for all KS residents)
2. Kansas also participates in IRS Direct File
3. Enter federal AGI as starting point
4. Subtract standard deduction ($3,605) and personal exemption ($9,160)
5. Calculate tax from KS brackets
6. Check Homestead Refund eligibility
7. Enter withholding from Box 17
8. Calculate refund or amount owed

## What to Tell the User

> "Kansas has two tax brackets (5.20% and 5.58%) with a $3,605 standard deduction and a generous $9,160 personal exemption -- combined, your first ~$12,765 is deducted from income. Lower-income renters may qualify for a Homestead Refund (Form K-40H). File for free at kansas.gov/webfile or via IRS Direct File."
