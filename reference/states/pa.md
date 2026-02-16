# Pennsylvania State Tax Reference

## Overview

Pennsylvania has one of the simplest state income tax systems in the country: a flat tax rate on all taxable compensation.

| Parameter | Value |
|---|---|
| Tax rate | **3.07%** (flat) |
| Form | PA-40 |
| Filing deadline | April 15 (same as federal) |
| Follows federal AGI? | **No** -- PA has its own definition of taxable income |
| Standard deduction | **None** -- PA does not offer a standard deduction |
| Personal exemption | **None** |
| Free file available | Yes, at https://www.revenue.pa.gov/ (PA e-File) |

## How PA Tax Works

### PA Taxable Compensation (Different from Federal)

PA does NOT start from federal AGI. Instead, PA has its own 8 classes of income:
1. Compensation (wages, salaries, tips, fees, commissions)
2. Net income from business
3. Net gains from property sales
4. Net income from rents, royalties, patents
5. Dividends
6. Interest
7. Gambling/lottery winnings
8. Net income from estates and trusts

**For EZFile's target user (W-2 only):** Only Class 1 (Compensation) applies.

### PA Compensation vs. Federal Box 1

PA taxable compensation (W-2 Box 16) often **differs** from federal wages (Box 1):

| Item | Federal (Box 1) | PA (Box 16) |
|---|---|---|
| Base salary | Included | Included |
| Pre-tax 401(k)/403(b) | Excluded | **Included** (PA taxes retirement contributions) |
| Pre-tax health insurance | Excluded | Excluded |
| Pre-tax HSA (employer) | Excluded | Excluded |
| Pre-tax FSA | Excluded | Excluded |
| Group term life >$50K | Included | Included |

This is why Box 16 (PA state wages) is typically **higher** than Box 1 (federal wages). In the sample W-2:
- Box 1 (federal): $44,629.35
- Box 16 (PA): $47,808.35
- Difference: $3,179.00 (largely the $4,107 retirement contribution minus other adjustments)

### Calculation

```
PA_taxable_income = W-2 Box 16 (state wages)
PA_tax = PA_taxable_income * 0.0307
PA_withheld = W-2 Box 17
PA_refund_or_owed = PA_withheld - PA_tax
```

### Sample Calculation

```
PA taxable income:  $47,808.35
PA tax rate:        × 3.07%
PA tax owed:        $1,467.72
PA withheld:        $1,467.72
PA refund/owed:     $0.00 (exact match)
```

## Local Taxes (Earned Income Tax / EIT)

Pennsylvania is one of the few states with widespread **local income taxes**. Nearly all municipalities and school districts levy an Earned Income Tax (EIT).

### W-2 Boxes 18-20
- Box 18: Local wages (usually same as Box 16)
- Box 19: Local tax withheld
- Box 20: Locality name or PSD code (Political Subdivision Code)

### Common Local Tax Rates
| Location | Rate | Notes |
|---|---|---|
| Pittsburgh | 3.0% | Includes 1% city + 2% school district |
| Philadelphia | 3.75% | Resident rate (non-resident: 3.44%) |
| Most PA municipalities | 1.0% - 2.0% | Combined municipal + school district |

### Local Tax Handling

For most PA localities:
```
local_tax_owed = Box 18 * local_rate
local_withheld = Box 19
local_refund_or_owed = local_withheld - local_tax_owed
```

**Note:** If Box 19 matches the expected local tax, the user typically does not need to file a separate local return (the employer handled it). If there's a discrepancy, the user may need to file with their local tax collector (identified by Box 20).

## PA Deductions and Credits

### No Standard Deduction
PA does NOT offer a standard deduction or personal exemption. The flat 3.07% applies to ALL compensation.

### PA Tax Forgiveness (Credit)
Low-income PA filers may qualify for Tax Forgiveness:

| Eligibility Income | Forgiveness |
|---|---|
| Single, $6,500 or less | 100% |
| Single, $6,501-$13,000 | Sliding scale (90% down to 10%) |

**EZFile note:** Most W-2 filers in this plugin's target demographic earn too much to qualify, but check for part-year or very low-wage workers.

### Student Loan Interest
PA does **not** allow a student loan interest deduction at the state level. The deduction only applies to the federal return.

### Schedule 1-A Deductions
PA treatment of Schedule 1-A deductions (tips, overtime, car loan, senior): PA does not conform to these federal deductions. They apply only to the federal return.

## Filing PA State Return

### PA-40 Form
1. Go to PA e-File: https://www.revenue.pa.gov/
2. Or use Free File Fillable Forms if PA-40 is available
3. Enter compensation from Box 16
4. Apply 3.07% rate
5. Enter withholding from Box 17
6. Calculate refund or amount owed

### Key PA-40 Lines
| PA-40 Line | Description | Source |
|---|---|---|
| Line 1a | Compensation | W-2 Box 16 |
| Line 9 | Total PA taxable income | Line 1a (for W-2 only filers) |
| Line 12 | PA tax | Line 9 × 3.07% |
| Line 13 | Total tax liability | Line 12 |
| Line 24 | PA tax withheld | W-2 Box 17 |
| Line 27 | Total payments/credits | Line 24 |
| Line 28 | Overpayment (if Line 27 > Line 13) | Refund |
| Line 30 | Amount owed (if Line 13 > Line 27) | Owed |

## What to Tell the User

> "Pennsylvania uses a flat 3.07% tax rate on your compensation -- no brackets, no standard deduction, just a simple percentage. Your PA wages ($XX,XXX from Box 16) are higher than your federal wages ($XX,XXX from Box 1) because PA taxes your retirement contributions that the federal government doesn't."
