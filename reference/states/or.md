# Oregon State Tax Reference

## Overview

Oregon has a progressive income tax with 4 brackets and some of the highest top rates in the country. Oregon has NO sales tax, so income tax is the primary revenue source.

| Parameter | Value |
|---|---|
| Tax type | Progressive (4 brackets) |
| Form | OR-40 (resident) |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- OR starts from federal AGI (with adjustments) |
| Standard deduction (Single) | **$2,835** (2025) |
| Personal exemption credit | **$256** (nonrefundable, income-limited to AGI ≤ $100,000) |
| Free file available | Yes, at https://www.oregon.gov/dor/ (Direct File Oregon) |

## OR Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $4,400 | 4.75% |
| $4,401 - $11,100 | 6.75% |
| $11,101 - $125,000 | 8.75% |
| Over $125,000 | 9.90% |

**For EZFile's target user:** The first 3 brackets are most relevant. Note: the 8.75% rate applies to most income for typical W-2 filers.

### Bracket Computation (Single)

```
if or_taxable <= 4,400:
    or_tax = or_taxable * 0.0475
elif or_taxable <= 11,100:
    or_tax = 209.00 + (or_taxable - 4,400) * 0.0675
elif or_taxable <= 125,000:
    or_tax = 661.25 + (or_taxable - 11,100) * 0.0875
else:
    or_tax = 10,627.50 + (or_taxable - 125,000) * 0.099
```

## Calculation

### Step 1: Start from Federal AGI
OR begins with federal AGI (Form 1040, Line 11). Oregon has its own additions and subtractions.

### Step 2: OR Standard Deduction
- Single: **$2,835** (2025, one of the lowest in the country)
- Additional $1,200 if age 65+ or blind

### Step 3: OR Taxable Income
```
OR_taxable = OR_AGI - OR_standard_deduction ($2,835)
OR_taxable = max(OR_taxable, 0)
```

### Step 4: Apply Brackets

### Step 5: Personal Exemption Credit
- **$256** per qualifying exemption (nonrefundable)
- Available if AGI ≤ $100,000 (single); phases out above this

### Step 6: Federal Tax Subtraction
Oregon allows a limited subtraction for **federal tax liability**:
- Maximum subtraction: **$7,650** (single, 2025 estimated)
- This reduces OR taxable income before brackets are applied

### Step 7: Compare to Withholding
```
OR_withheld = W-2 Box 17
OR_refund_or_owed = OR_withheld - OR_tax
```

### Sample Calculation (Federal AGI of $42,829, Federal Tax of $3,968)

```
OR AGI:                $42,829.35
Standard deduction:    -$2,835.00
Federal tax subtraction: -$3,967.50 (up to $7,650 cap)
OR taxable income:     $36,026.85

OR tax calculation:
  4.75% on $4,400:        $209.00
  6.75% on $6,700:        $452.25
  8.75% on $24,926.85:  $2,181.10
OR gross tax:          $2,842.35
Personal credit:          -$256.00
OR net tax:            $2,586.35

OR withheld (Box 17):  $X,XXX.XX
OR refund/owed:        calculated
```

## OR Deductions and Credits

### Standard Deduction
OR's standard deduction ($2,835 single) is one of the lowest in the country.

### Federal Tax Subtraction
Oregon allows a subtraction for federal income tax liability, capped at **$7,650** (single, estimated). This partially offsets the high state rates.

### Personal Exemption Credit
$256 nonrefundable credit per person, available if AGI ≤ $100,000.

### No Sales Tax
Oregon has no sales tax -- income tax is the state's primary revenue source.

### Renter Benefit
OR does **not** offer a general renter's credit or deduction.

### Earned Income Credit
- OR offers its own EIC equal to **12%** of the federal EIC (refundable)
- If the user qualifies for federal EIC, they also get the OR EIC

### Kicker Refund
Oregon has a unique "kicker" -- when state revenue exceeds forecasts by more than 2%, the surplus is returned to taxpayers as a credit. This varies by year.

### Student Loan Interest
OR does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

## Filing OR State Return

### Form OR-40
1. Go to https://www.oregon.gov/dor/ (Direct File Oregon -- free combined federal/state)
2. Enter federal AGI as starting point
3. Subtract standard deduction ($2,835)
4. Subtract federal tax liability (up to $7,650)
5. Calculate tax from OR brackets
6. Subtract $256 personal credit
7. Check for kicker credit
8. Enter withholding from Box 17
9. Calculate refund or amount owed

## What to Tell the User

> "Oregon has high tax rates (4.75%-9.90%) and a very small standard deduction ($2,835), but you can subtract some of your federal tax (up to $7,650) and get a $256 personal credit. Oregon has no sales tax. Oregon participates in IRS Direct File for free combined filing at oregon.gov/dor."
