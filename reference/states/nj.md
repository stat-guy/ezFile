# New Jersey State Tax Reference

## Overview

New Jersey has a progressive income tax with 7 brackets. NJ uses its **own income definition** -- it does NOT start from federal AGI.

| Parameter | Value |
|---|---|
| Tax type | Progressive (7 brackets) |
| Form | NJ-1040 |
| Filing deadline | April 15 |
| Follows federal AGI? | **No** -- NJ has its own gross income definition |
| Standard deduction | **None** |
| Personal exemption | **$1,000** (single) |
| Free file available | Yes, at https://www.nj.gov/treasury/taxation/ (NJ E-File) |

## NJ Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $20,000 | 1.40% |
| $20,001 - $35,000 | 1.75% |
| $35,001 - $40,000 | 3.50% |
| $40,001 - $75,000 | 5.525% |
| $75,001 - $500,000 | 6.37% |
| $500,001 - $1,000,000 | 8.97% |
| Over $1,000,000 | 10.75% |

**For EZFile's target user:** The first 4-5 brackets (up to $75,000) are most relevant.

### Bracket Computation (Single)

```
if nj_taxable <= 20,000:
    nj_tax = nj_taxable * 0.014
elif nj_taxable <= 35,000:
    nj_tax = 280 + (nj_taxable - 20,000) * 0.0175
elif nj_taxable <= 40,000:
    nj_tax = 542.50 + (nj_taxable - 35,000) * 0.035
elif nj_taxable <= 75,000:
    nj_tax = 717.50 + (nj_taxable - 40,000) * 0.05525
elif nj_taxable <= 500,000:
    nj_tax = 2,651.25 + (nj_taxable - 75,000) * 0.0637
else:
    # Higher brackets exist but unlikely for this profile
    nj_tax = 29,723.75 + (nj_taxable - 500,000) * 0.0897
```

## How NJ Tax Works

### Starting Point: NJ Gross Income (Not Federal AGI)

NJ has its **own definition of gross income**. Key differences from federal:

| Item | Federal Treatment | NJ Treatment |
|---|---|---|
| Wages (W-2 Box 1) | Included | Included |
| Pre-tax 401(k)/403(b) | Excluded from Box 1 | **Included** (NJ taxes retirement contributions) |
| Student loan interest | Deducted on federal | **Not deductible** in NJ |
| Schedule 1-A deductions | Deducted on federal | **Not applicable** in NJ |

**For EZFile's target user (W-2 only):** Use W-2 Box 16 (state wages) if available. If Box 16 shows NJ, this is the NJ gross income basis. If Box 16 is blank, use Box 1 but note NJ may tax retirement contributions differently.

### Personal Exemption

- Single: **$1,000**
- Very small -- effectively just $1,000 off taxable income

### Calculation

```
NJ_gross_income = W-2 Box 16 (NJ state wages) or Box 1
NJ_taxable_income = NJ_gross_income - personal_exemption ($1,000)
NJ_taxable_income = max(NJ_taxable_income, 0)
NJ_tax = apply brackets to NJ_taxable_income
NJ_withheld = W-2 Box 17
NJ_refund_or_owed = NJ_withheld - NJ_tax
```

### Sample Calculation (NJ Wages of $47,808)

```
NJ gross income:       $47,808.35
Personal exemption:    -$1,000.00
NJ taxable income:     $46,808.35

NJ tax calculation:
  1.40% on $20,000:       $280.00
  1.75% on $15,000:       $262.50
  3.50% on $5,000:        $175.00
  5.525% on $6,808.35:    $376.16
NJ gross tax:            $1,093.66

NJ withheld (Box 17):   $X,XXX.XX
NJ refund/owed:         calculated
```

## NJ Deductions and Credits

### No Standard Deduction
NJ does NOT offer a standard deduction. Only the $1,000 personal exemption applies.

### Property Tax Deduction/Credit (Renters!)
- NJ treats **18% of rent paid** as property tax
- This 18% amount can be claimed as a **property tax deduction** (up to $15,000) on the NJ return
- **This applies to EZFile's target user!** Always ask about rent paid.
- Example: If rent is $1,200/month ($14,400/year), the deduction is $14,400 × 18% = $2,592

### Earned Income Tax Credit
- NJ offers its own EIC equal to **40%** of the federal EIC
- If the user qualifies for federal EIC, they also get the NJ EIC
- One of the most generous state EICs

### Student Loan Interest
NJ does **not** allow a student loan interest deduction. This deduction applies only to the federal return.

### NJ Filing Threshold
- Single under 65: must file if gross income exceeds **$10,000**
- Most W-2 filers will be above this threshold

## Filing NJ State Return

### NJ-1040 Form
1. Go to https://www.nj.gov/treasury/taxation/ (NJ E-File)
2. Free e-filing available for NJ residents
3. Enter NJ gross income (Box 16 or calculated)
4. Subtract personal exemption ($1,000)
5. Subtract property tax deduction (18% of rent if renting)
6. Calculate tax from NJ brackets
7. Enter withholding from Box 17
8. Calculate refund or amount owed

## What to Tell the User

> "New Jersey has its own income definition (not federal AGI) and progressive brackets from 1.4% to 10.75%. NJ's personal exemption is only $1,000, but renters get a valuable benefit: 18% of your rent counts as a property tax deduction. File for free at nj.gov/treasury/taxation."
