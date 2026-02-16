# Louisiana State Tax Reference

## Overview

Louisiana completely reformed its income tax for 2025, replacing 3 progressive brackets with a single flat rate. This is a brand-new system.

| Parameter | Value |
|---|---|
| Tax rate | **3.0%** (flat, new for 2025) |
| Form | IT-540 |
| Filing deadline | May 15 (Louisiana's deadline is later than most states!) |
| Follows federal AGI? | **Yes** -- LA starts from federal AGI |
| Standard deduction (Single) | **$12,500** (new for 2025) |
| Personal exemption | **None** (eliminated in 2025 reform) |
| Free file available | Yes, at https://latap.revenue.louisiana.gov/ (LaTAP) |

## How LA Tax Works

### Starting Point: Federal AGI

Louisiana begins with federal AGI (Form 1040, Line 11).

### Standard Deduction (New for 2025)

The 2025 reform replaced the old personal exemption system with a new standard deduction:
- Single: **$12,500**
- Subject to annual inflation adjustments starting 2026

### Calculation

```
LA_AGI = Federal AGI (Form 1040, Line 11)
LA_taxable_income = LA_AGI - LA_standard_deduction ($12,500)
LA_taxable_income = max(LA_taxable_income, 0)
LA_tax = LA_taxable_income * 0.03
LA_withheld = W-2 Box 17
LA_refund_or_owed = LA_withheld - LA_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
LA AGI:                $42,829.35
Standard deduction:   -$12,500.00
LA taxable income:     $30,329.35

LA tax rate:           × 3.0%
LA tax owed:             $909.88

LA withheld (Box 17):  $X,XXX.XX
LA refund/owed:        calculated
```

## What Changed in 2025

| Feature | Pre-2025 (Old System) | 2025+ (New System) |
|---|---|---|
| Rate structure | 3 brackets (1.85%, 3.5%, 4.25%) | Flat 3.0% |
| Standard deduction | None | $12,500 (single) |
| Personal exemption | $4,500 (single) + credits | None |

## LA Deductions and Credits

### Standard Deduction
LA's new $12,500 standard deduction is relatively generous and simplifies the calculation significantly.

### Renter Benefit
LA does **not** offer a renter's credit or deduction.

### Earned Income Credit
- LA offers its own EIC equal to **5%** of the federal EIC
- If the user qualifies for federal EIC, they also get the LA EIC

### Student Loan Interest
LA does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

## Filing LA State Return

### IT-540 Form
1. Go to https://latap.revenue.louisiana.gov/ (LaTAP)
2. Free e-filing available for LA residents
3. **Note: LA deadline is May 15** (not April 15!)
4. Enter federal AGI as starting point
5. Subtract standard deduction ($12,500)
6. Apply 3.0% flat rate
7. Enter withholding from Box 17
8. Calculate refund or amount owed

## What to Tell the User

> "Louisiana completely reformed its income tax for 2025 -- it's now a simple flat 3.0% rate with a $12,500 standard deduction (replacing the old 3-bracket system). One of the lowest income tax rates in the country. Important: Louisiana's filing deadline is **May 15**. File for free at latap.revenue.louisiana.gov."
