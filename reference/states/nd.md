# North Dakota State Tax Reference

## Overview

North Dakota recently reformed its tax system into a near-zero-tax state for most filers. The first $48,475 of taxable income is completely tax-free.

| Parameter | Value |
|---|---|
| Tax type | Progressive (3 brackets, first is 0%) |
| Form | ND-1 |
| Filing deadline | April 15 |
| Follows federal AGI? | **No** -- ND starts from federal **taxable income** (Line 15) |
| Standard deduction | **None** (uses federal standard deduction indirectly) |
| Free file available | Yes, at https://www.tax.nd.gov/ (Free File Alliance) |

## ND Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $48,475 | 0.00% |
| $48,476 - $244,825 | 1.95% |
| Over $244,825 | 2.50% |

**Key insight:** A single filer effectively pays NO ND tax until federal taxable income exceeds $48,475. Combined with the federal standard deduction ($15,750), gross income would need to exceed ~$64,225 before any ND tax is owed.

## How ND Tax Works

### Starting Point: Federal Taxable Income (Line 15)

ND starts from **federal taxable income** (Form 1040, Line 15). The federal standard deduction is already subtracted.

### Calculation

```
ND_taxable = Federal taxable income (Form 1040, Line 15)
# ND-specific adjustments may apply

if ND_taxable <= 48,475:
    ND_tax = 0
elif ND_taxable <= 244,825:
    ND_tax = (ND_taxable - 48,475) * 0.0195
else:
    ND_tax = 3,828.83 + (ND_taxable - 244,825) * 0.025

ND_withheld = W-2 Box 17
ND_refund_or_owed = ND_withheld - ND_tax
```

### Sample Calculation (Federal Taxable Income of $27,079)

```
Federal taxable income (Line 15): $27,079.35
Amount in 0% bracket:             $27,079.35 (below $48,475)
ND tax owed:                       $0.00

ND withheld (Box 17):             $XXX.XX
ND refund:                        full refund of withholding
```

**For EZFile's target demographic:** Most single filers with AGI under ~$64,000 will owe NO ND tax.

## ND Deductions and Credits

### Near-Zero Effective Tax
With the $48,475 zero-bracket and starting from federal taxable income, most W-2 filers pay nothing.

### Renter Benefit
ND does **not** offer a general renter's credit or deduction. A Homestead Credit exists for **65+ or disabled** only.

### Earned Income Credit
- ND does **not** currently offer its own state EIC

### Student Loan Interest
ND does **not** allow a separate student loan interest deduction -- it's already reflected in federal taxable income.

## Filing ND State Return

### Form ND-1
1. Go to https://www.tax.nd.gov/ (Free File Alliance)
2. Enter federal taxable income (Form 1040, Line 15) as starting point
3. Apply ND adjustments
4. Calculate tax (0% on first $48,475, then 1.95%)
5. Enter withholding from Box 17
6. Calculate refund or amount owed

## What to Tell the User

> "North Dakota has one of the lowest income tax burdens in the country. The first $48,475 of taxable income is completely tax-free, and the rate above that is just 1.95%. At your income level, you likely owe NO ND tax and will get a full refund of state withholding. File for free at tax.nd.gov."
