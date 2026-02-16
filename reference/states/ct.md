# Connecticut State Tax Reference

## Overview

Connecticut has a progressive income tax with 7 brackets. It uses a personal exemption instead of a standard deduction, but the exemption phases out rapidly.

| Parameter | Value |
|---|---|
| Tax type | Progressive (7 brackets) |
| Form | CT-1040 |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- CT starts from federal AGI |
| Standard deduction | **None** |
| Personal exemption | **$15,000** (single), phases out rapidly above ~$30K AGI |
| Free file available | Yes, at https://portal.ct.gov/drs (myconneCT) |

## CT Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $10,000 | 2.00% |
| $10,001 - $50,000 | 4.50% |
| $50,001 - $100,000 | 5.50% |
| $100,001 - $200,000 | 6.00% |
| $200,001 - $250,000 | 6.50% |
| $250,001 - $500,000 | 6.90% |
| Over $500,000 | 6.99% |

**For EZFile's target user:** The first 3 brackets (up to $100,000) are most relevant.

### Bracket Computation (Single)

```
if ct_taxable <= 10,000:
    ct_tax = ct_taxable * 0.02
elif ct_taxable <= 50,000:
    ct_tax = 200 + (ct_taxable - 10,000) * 0.045
elif ct_taxable <= 100,000:
    ct_tax = 2,000 + (ct_taxable - 50,000) * 0.055
elif ct_taxable <= 200,000:
    ct_tax = 4,750 + (ct_taxable - 100,000) * 0.06
elif ct_taxable <= 250,000:
    ct_tax = 10,750 + (ct_taxable - 200,000) * 0.065
elif ct_taxable <= 500,000:
    ct_tax = 14,000 + (ct_taxable - 250,000) * 0.069
else:
    ct_tax = 31,250 + (ct_taxable - 500,000) * 0.0699
```

## Calculation

### Step 1: Start from Federal AGI
CT begins with the federal AGI (Form 1040, Line 11).

### Step 2: CT Modifications
For W-2-only filers, typically no modifications needed. CT AGI usually equals federal AGI.

### Step 3: Personal Exemption (Phases Out Fast)

CT's personal exemption is generous at lower incomes but disappears quickly:

| CT AGI (Single) | Exemption Amount |
|---|---|
| $0 - $15,000 | $15,000 (full) |
| $15,001 - $20,000 | $14,000 |
| $20,001 - $25,000 | $13,000 |
| $25,001 - $30,000 | $12,000 |
| $30,001 - $35,000 | $11,000 |
| $35,001 - $40,000 | $10,000 |
| $40,001 - $44,500 | $9,000 |
| $44,501+ | $0 (fully phased out) |

**Key insight:** For most W-2 filers earning above ~$44,500, the personal exemption is **completely gone**. This effectively means CT taxes your full AGI.

### Step 4: CT Taxable Income
```
CT_taxable = CT_AGI - CT_personal_exemption
CT_taxable = max(CT_taxable, 0)
```

### Step 5: Apply Brackets
Use the bracket table above.

### Step 6: CT Tax Credit (Reduces Tax)
CT also applies a tax credit that reduces the calculated tax for lower-income filers:
- If CT AGI ≤ $30,000 (single): 75% credit (pay only 25% of bracket tax)
- Phases out between $30,000 and $64,000
- Above $64,000: no credit

### Step 7: Compare to Withholding
```
CT_withheld = W-2 Box 17
CT_refund_or_owed = CT_withheld - CT_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
CT AGI:                    $42,829.35
Personal exemption:        -$9,000.00 (phased down at this income)
CT taxable income:         $33,829.35

CT tax calculation:
  2.00% on $10,000:          $200.00
  4.50% on $23,829.35:    $1,072.32
CT gross tax:              $1,272.32

CT tax credit:             may apply (partial, phases out at this AGI)
CT net tax:                ~$1,000-$1,272 depending on credit

CT withheld (Box 17):      $X,XXX.XX
CT refund/owed:            calculated
```

## CT Deductions and Credits

### No Standard Deduction
CT does NOT offer a standard deduction. The personal exemption serves a similar role but phases out entirely above ~$44,500 AGI.

### Property Tax Credit
- For property taxpayers (homeowners) only -- $200 max
- NOT applicable to EZFile's target user (renters)

### Renter Benefit
- CT offers a renter's rebate ONLY for **elderly (65+) or disabled** residents
- NOT applicable to most of EZFile's target users

### Earned Income Tax Credit
- CT offers its own EIC equal to **41.5%** of the federal EIC
- If the user qualifies for federal EIC, they also get the CT EIC
- One of the most generous state EICs

### Student Loan Interest
CT does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

## Filing CT State Return

### CT-1040 Form
1. Go to https://portal.ct.gov/drs (myconneCT)
2. Free e-filing available for CT residents
3. Enter federal AGI as starting point
4. Apply personal exemption (check phaseout table)
5. Calculate tax from brackets
6. Apply CT tax credit if eligible
7. Enter withholding from Box 17
8. Calculate refund or amount owed

## What to Tell the User

> "Connecticut has progressive tax brackets (2%-6.99%) and a personal exemption that phases out quickly -- if you earn above ~$44,500, you get no exemption at all. The good news: CT has a generous tax credit for lower-income filers that can significantly reduce your bill. File for free at portal.ct.gov/drs."
