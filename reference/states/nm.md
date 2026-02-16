# New Mexico State Tax Reference

## Overview

New Mexico has a progressive income tax with 6 brackets (reformed via HB 252, 2024) and offers a Low-Income Comprehensive Tax Rebate for qualifying filers.

| Parameter | Value |
|---|---|
| Tax type | Progressive (6 brackets) |
| Form | PIT-1 |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- NM starts from federal AGI |
| Standard deduction (Single) | Uses federal standard deduction (~$15,750) |
| Personal exemption | **$2,500** (for low/middle income filers) |
| Free file available | Yes, at https://tap.state.nm.us/ (Taxpayer Access Point + IRS Direct File) |

## NM Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $5,500 | 1.50% |
| $5,501 - $16,500 | 3.20% |
| $16,501 - $33,500 | 4.30% |
| $33,501 - $66,500 | 4.70% |
| $66,501 - $210,000 | 4.90% |
| Over $210,000 | 5.90% |

**For EZFile's target user:** The first 4 brackets are most relevant.

### Bracket Computation (Single)

```
if nm_taxable <= 5,500:
    nm_tax = nm_taxable * 0.015
elif nm_taxable <= 16,500:
    nm_tax = 82.50 + (nm_taxable - 5,500) * 0.032
elif nm_taxable <= 33,500:
    nm_tax = 434.50 + (nm_taxable - 16,500) * 0.043
elif nm_taxable <= 66,500:
    nm_tax = 1,165.50 + (nm_taxable - 33,500) * 0.047
elif nm_taxable <= 210,000:
    nm_tax = 2,716.50 + (nm_taxable - 66,500) * 0.049
else:
    nm_tax = 9,748.00 + (nm_taxable - 210,000) * 0.059
```

## Calculation

### Step 1: Start from Federal AGI
NM begins with federal AGI (Form 1040, Line 11).

### Step 2: NM Deductions
- Standard deduction: Uses federal amount (~**$15,750** single, 2025)
- Personal exemption: **$2,500** (may be income-limited for higher earners)

### Step 3: NM Taxable Income
```
NM_taxable = NM_AGI - NM_standard_deduction (~$15,750) - NM_personal_exemption ($2,500)
NM_taxable = max(NM_taxable, 0)
```

### Step 4: Apply Brackets

### Step 5: Compare to Withholding

### Sample Calculation (Federal AGI of $42,829)

```
NM AGI:                $42,829.35
Standard deduction:   -$15,750.00
Personal exemption:    -$2,500.00
NM taxable income:     $24,579.35

NM tax calculation:
  1.50% on $5,500:        $82.50
  3.20% on $11,000:      $352.00
  4.30% on $8,079.35:    $347.41
NM tax:                  $781.91

NM withheld (Box 17):  $X,XXX.XX
NM refund/owed:        calculated
```

## NM Deductions and Credits

### Low-Income Comprehensive Tax Rebate (LICTR)
- Available to NM residents with **modified gross income ≤ $36,000**
- Must have been present in NM for at least 6 months
- Rebate amount varies by income and filing status
- **Check for lower-income EZFile users**

### Property Tax Rebate (65+ Only)
- For residents age 65+ with income ≤ $16,000
- Maximum $250 (single)
- NOT applicable to most EZFile users

### Renter Benefit
NM does **not** offer a general renter's credit. The Property Tax Rebate is limited to 65+ residents.

### Earned Income Credit
- NM offers its own EIC equal to **25%** of the federal EIC
- If the user qualifies for federal EIC, they also get the NM EIC

### Student Loan Interest
NM does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

## Filing NM State Return

### Form PIT-1
1. Go to https://tap.state.nm.us/ (Taxpayer Access Point) or via IRS Direct File
2. Enter federal AGI as starting point
3. Subtract standard deduction and personal exemption
4. Calculate tax from NM brackets
5. Check LICTR eligibility if income ≤ $36,000
6. Enter withholding from Box 17
7. Calculate refund or amount owed

## What to Tell the User

> "New Mexico has progressive brackets (1.50%-5.90%) and uses the federal standard deduction plus a $2,500 personal exemption. If your income is under $36,000, check if you qualify for the Low-Income Comprehensive Tax Rebate. NM participates in IRS Direct File. File at tap.state.nm.us."
