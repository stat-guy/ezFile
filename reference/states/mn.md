# Minnesota State Tax Reference

## Overview

Minnesota has a progressive income tax with 4 brackets and some of the highest rates in the country. MN starts from **federal taxable income** (Line 15) and offers a significant Renter's Property Tax Refund.

| Parameter | Value |
|---|---|
| Tax type | Progressive (4 brackets) |
| Form | M1 |
| Filing deadline | April 15 |
| Follows federal AGI? | **No** -- MN starts from federal **taxable income** (Line 15) |
| Standard deduction | **None** (uses federal standard deduction indirectly) |
| Renter's refund | Filed separately on Form M1PR |
| Free file available | Yes, at https://www.revenue.state.mn.us/ |

## MN Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $31,690 | 5.35% |
| $31,691 - $104,090 | 6.80% |
| $104,091 - $183,340 | 7.85% |
| Over $183,340 | 9.85% |

**For EZFile's target user:** The first 1-2 brackets are most relevant.

### Bracket Computation (Single)

```
if mn_taxable <= 31,690:
    mn_tax = mn_taxable * 0.0535
elif mn_taxable <= 104,090:
    mn_tax = 1,695.42 + (mn_taxable - 31,690) * 0.068
elif mn_taxable <= 183,340:
    mn_tax = 6,618.62 + (mn_taxable - 104,090) * 0.0785
else:
    mn_tax = 12,839.74 + (mn_taxable - 183,340) * 0.0985
```

## Calculation

### Step 1: Start from Federal Taxable Income (Line 15)

Minnesota starts from **federal taxable income** (Form 1040, Line 15), like Colorado and Vermont. The federal standard deduction is already subtracted.

### Step 2: MN Modifications
MN has some additions and subtractions but for W-2-only filers, MN taxable income typically equals federal taxable income.

### Step 3: No Additional Deduction
Because MN starts after the federal standard deduction, there is no MN-specific standard deduction.

### Step 4: Apply Brackets
Use the bracket table above.

### Step 5: Compare to Withholding
```
MN_taxable = Federal taxable income (Form 1040, Line 15)
MN_tax = apply brackets
MN_withheld = W-2 Box 17
MN_refund_or_owed = MN_withheld - MN_tax
```

### Sample Calculation (Federal Taxable Income of $27,079)

```
Federal taxable income (Line 15): $27,079.35
MN tax (5.35%):                    $1,448.75

MN withheld (Box 17):             $X,XXX.XX
MN refund/owed:                   calculated
```

## MN Deductions and Credits

### No Standard Deduction
MN does NOT offer its own standard deduction. Because it starts from federal taxable income, the federal standard deduction ($15,750) is already applied.

### Renter's Property Tax Refund (Form M1PR -- Important!)
- Available to MN renters with **household income ≤ $69,520** (approximately)
- For renters: **17% of rent paid** is treated as property tax
- Refund is based on the amount by which property tax exceeds a percentage of income
- Can be **very significant** -- up to **$2,270** for qualifying renters
- **Filed separately** on Form M1PR (not part of the income tax return)
- Filing deadline: **August 15** (later than the income tax return!)
- **This is a major benefit for EZFile's target user!** Always mention it.

**Example:**
```
Annual rent: $12,000
Property tax equivalent: $12,000 × 17% = $2,040
Refund depends on income-based formula (lower income = higher refund)
```

### Working Family Credit (MN's EIC)
- MN offers its own version of the EIC called the Working Family Credit
- Generally **more generous** than a simple percentage of the federal EIC
- If the user qualifies for federal EIC, check MN Working Family Credit too

### Student Loan Interest
MN does **not** allow a separate student loan interest deduction -- it's already reflected in federal taxable income.

## Filing MN State Return

### Form M1
1. Go to https://www.revenue.state.mn.us/
2. Free e-filing available for MN residents
3. Enter federal taxable income (Form 1040, Line 15) as starting point
4. Apply MN brackets
5. Enter withholding from Box 17
6. Calculate refund or amount owed
7. **Separately:** File Form M1PR for Renter's Property Tax Refund (deadline August 15!)

## What to Tell the User

> "Minnesota starts from your federal taxable income (Line 15) and has progressive brackets (5.35%-9.85%). Very important for renters: Minnesota offers a Renter's Property Tax Refund (up to ~$2,270) filed separately on Form M1PR -- the deadline is August 15, so you have extra time. 17% of your rent counts as property tax for this refund. File your income tax return at revenue.state.mn.us, and don't forget the M1PR!"
