# Maine State Tax Reference

## Overview

Maine has a progressive income tax with 3 brackets and a standard deduction that matches the federal amount.

| Parameter | Value |
|---|---|
| Tax type | Progressive (3 brackets) |
| Form | 1040ME |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- ME starts from federal AGI |
| Standard deduction (Single) | **$15,750** (matches federal, 2025) |
| Free file available | Yes, at https://www.maine.gov/revenue/ (Maine FastFile) |

## ME Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $26,050 | 5.80% |
| $26,051 - $61,600 | 6.75% |
| Over $61,600 | 7.15% |

**For EZFile's target user:** The first 2 brackets (up to $61,600) are most relevant.

### Bracket Computation (Single)

```
if me_taxable <= 26,050:
    me_tax = me_taxable * 0.058
elif me_taxable <= 61,600:
    me_tax = 1,510.90 + (me_taxable - 26,050) * 0.0675
else:
    me_tax = 3,910.03 + (me_taxable - 61,600) * 0.0715
```

## Calculation

### Step 1: Start from Federal AGI
ME begins with the federal AGI (Form 1040, Line 11).

### Step 2: ME Modifications
For W-2-only filers, ME AGI typically equals federal AGI. ME generally conforms to federal definitions.

### Step 3: ME Standard Deduction
- Single: **$15,750** (2025, matches federal)
- Single 65+: **$17,750** (2025, matches federal)

### Step 4: ME Taxable Income
```
ME_taxable = ME_AGI - ME_standard_deduction ($15,750)
ME_taxable = max(ME_taxable, 0)
```

### Step 5: Apply Brackets
Use the bracket table above.

### Step 6: Compare to Withholding
```
ME_withheld = W-2 Box 17
ME_refund_or_owed = ME_withheld - ME_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
ME AGI:                $42,829.35
Standard deduction:   -$15,750.00
ME taxable income:     $27,079.35

ME tax calculation:
  5.80% on $26,050:     $1,510.90
  6.75% on $1,029.35:      $69.48
ME tax:                $1,580.38

ME withheld (Box 17):  $X,XXX.XX
ME refund/owed:        calculated
```

## ME Deductions and Credits

### Standard Deduction
ME uses the same standard deduction as the federal government ($15,750 single, $17,750 single 65+). This simplifies the calculation.

### Property Tax Fairness Credit (Renters!)
- Available to ME renters AND homeowners
- For renters: **4% of rent paid** is treated as property tax paid
- Credit equals the amount by which property tax exceeds **6% of income**, up to **$1,000**
- Income limit: household income up to **$40,000** (single)
- **This may apply to EZFile's target users!** Check income and rent.

**Example:**
```
Annual rent: $12,000
Property tax equivalent: $12,000 × 4% = $480
6% of income ($42,829): $2,569.76
Credit = max($480 - $2,570, 0) = $0 (income too high in this example)

If income were $30,000:
6% of income: $1,800
Credit = max($480 - $1,800, 0) = $0 (still exceeds)
```

**Note:** The credit is most beneficial for very low-income filers with high rent relative to income.

### Earned Income Credit
- ME offers its own EIC equal to **12%** of the federal EIC
- If the user qualifies for federal EIC, they also get the ME EIC

### Student Loan Interest
ME does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

## Filing ME State Return

### Form 1040ME
1. Go to https://www.maine.gov/revenue/ (Maine FastFile)
2. Free e-filing available for ME residents
3. Enter federal AGI as starting point
4. Apply standard deduction ($15,750)
5. Calculate tax from ME brackets
6. Check Property Tax Fairness Credit eligibility
7. Enter withholding from Box 17
8. Calculate refund or amount owed

## What to Tell the User

> "Maine has three tax brackets (5.8%, 6.75%, and 7.15%) with a standard deduction that matches the federal amount ($15,750). Maine also offers a Property Tax Fairness Credit for renters -- if your income is under $40,000 and your rent is high relative to your income, you could get up to $1,000 back. File for free at maine.gov/revenue."
