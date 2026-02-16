# Vermont State Tax Reference

## Overview

Vermont has a progressive income tax with 4 brackets and starts from **federal taxable income** (Form 1040 Line 15), not federal AGI. Vermont also offers a Renter Rebate for qualifying renters.

| Parameter | Value |
|---|---|
| Tax type | Progressive (4 brackets) |
| Form | IN-111 |
| Filing deadline | April 15 |
| Follows federal AGI? | **No** -- VT starts from federal **taxable income** (Line 15) |
| Standard deduction | **None** (uses federal standard deduction indirectly) |
| Free file available | Yes, at https://tax.vermont.gov/ (myVTax) |

## VT Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $45,400 | 3.35% |
| $45,401 - $110,450 | 6.60% |
| $110,451 - $229,550 | 7.60% |
| Over $229,550 | 8.75% |

**For EZFile's target user:** The first 1-2 brackets are most relevant.

### Bracket Computation (Single)

```
if vt_taxable <= 45,400:
    vt_tax = vt_taxable * 0.0335
elif vt_taxable <= 110,450:
    vt_tax = 1,520.90 + (vt_taxable - 45,400) * 0.066
elif vt_taxable <= 229,550:
    vt_tax = 5,814.20 + (vt_taxable - 110,450) * 0.076
else:
    vt_tax = 14,865.80 + (vt_taxable - 229,550) * 0.0875
```

## Calculation

### Step 1: Start from Federal Taxable Income (Line 15)

Like Colorado, Vermont starts from **federal taxable income** (Form 1040, Line 15). This means the federal standard deduction is already subtracted before Vermont applies its brackets.

### Step 2: VT Modifications
For W-2-only filers, VT taxable income typically equals federal taxable income. Vermont may have some additions/subtractions but they rarely apply to simple W-2 filers.

### Step 3: No Additional Deduction
Because VT starts after the federal standard deduction, there is no VT-specific standard deduction or personal exemption. The brackets apply directly to federal taxable income.

### Step 4: Apply Brackets
Use the bracket table above.

### Step 5: Compare to Withholding
```
VT_taxable = Federal taxable income (Form 1040, Line 15)
VT_tax = apply brackets
VT_withheld = W-2 Box 17
VT_refund_or_owed = VT_withheld - VT_tax
```

### Sample Calculation (Federal Taxable Income of $27,079)

```
Federal taxable income (Line 15): $27,079.35
VT tax (3.35%):                     $907.16

VT withheld (Box 17):             $X,XXX.XX
VT refund/owed:                   calculated
```

## VT Deductions and Credits

### No Standard Deduction
VT does NOT offer its own standard deduction. Because it starts from federal taxable income, the federal standard deduction ($15,750) is already applied.

### Renter Rebate (Property Tax Credit for Renters!)
- Available to VT renters with **household income ≤ $47,000** (approximately)
- For renters: a portion of rent is treated as property tax
- Rebate calculated based on a percentage of income spent on rent/property tax
- Maximum rebate: approximately **$3,000**
- Filed on Form PR-141 (separate from income tax return)
- **This applies to EZFile's target user!** Always mention this benefit.

### Earned Income Credit
- VT offers its own EIC equal to **38%** of the federal EIC
- If the user qualifies for federal EIC, they also get the VT EIC
- One of the most generous state EICs

### Student Loan Interest
VT does **not** allow a separate student loan interest deduction -- it's already reflected in federal taxable income.

## Filing VT State Return

### Form IN-111
1. Go to https://tax.vermont.gov/ (myVTax)
2. Free e-filing available for VT residents
3. Enter federal taxable income (Form 1040, Line 15) as starting point
4. Apply VT brackets
5. Enter withholding from Box 17
6. Calculate refund or amount owed
7. **Separately:** File Form PR-141 for Renter Rebate if eligible

## What to Tell the User

> "Vermont starts from your federal taxable income (Line 15, after the standard deduction) and applies its own brackets (3.35%-8.75%). Important for renters: VT offers a Renter Rebate (up to ~$3,000) filed separately on Form PR-141 -- check eligibility at tax.vermont.gov if your household income is under $47,000. File for free at tax.vermont.gov."
