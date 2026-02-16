# Alabama State Tax Reference

## Overview

Alabama has a progressive income tax with 3 brackets and a unique feature: you can **deduct your federal income tax paid** from your Alabama taxable income.

| Parameter | Value |
|---|---|
| Tax type | Progressive (3 brackets) |
| Form | 40 (resident) |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- AL starts from federal AGI |
| Standard deduction (Single) | **$3,000** |
| Personal exemption | **$1,500** |
| Unique feature | **Federal income tax is deductible** from AL taxable income |
| Free file available | Yes, at https://www.revenue.alabama.gov/ (My Alabama Taxes) |

## AL Tax Brackets (Single, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $500 | 2.00% |
| $501 - $3,000 | 4.00% |
| Over $3,000 | 5.00% |

**Key insight:** The top rate (5%) kicks in at just $3,001 of taxable income. For most W-2 filers, the effective rate is very close to 5% on nearly all taxable income.

### Bracket Computation (Single)

```
if al_taxable <= 500:
    al_tax = al_taxable * 0.02
elif al_taxable <= 3,000:
    al_tax = 10 + (al_taxable - 500) * 0.04
else:
    al_tax = 110 + (al_taxable - 3,000) * 0.05
```

## How AL Tax Works

### Starting Point: Federal AGI
AL begins with federal AGI (Form 1040, Line 11).

### Federal Tax Deduction (Unique!)
Alabama is one of very few states that allows you to **deduct your federal income tax liability** from your state taxable income. This significantly reduces the AL tax bill.

For EZFile's profile, this means deducting Line 24 (total federal tax) from AL income.

### Calculation

```
AL_AGI = Federal AGI (Form 1040, Line 11)
AL_federal_tax_deduction = Federal total tax (Form 1040, Line 24)
AL_std_deduction = $3,000
AL_personal_exemption = $1,500

AL_taxable_income = AL_AGI - AL_federal_tax_deduction - AL_std_deduction - AL_personal_exemption
AL_taxable_income = max(AL_taxable_income, 0)
AL_tax = apply brackets to AL_taxable_income
AL_withheld = W-2 Box 17
AL_refund_or_owed = AL_withheld - AL_tax
```

### Sample Calculation (Federal AGI of $42,829, Federal Tax of $3,968)

```
AL AGI:                    $42,829.35
Federal tax deduction:     -$3,967.50
Standard deduction:        -$3,000.00
Personal exemption:        -$1,500.00
AL taxable income:         $34,361.85

AL tax calculation:
  2.00% on $500:               $10.00
  4.00% on $2,500:            $100.00
  5.00% on $31,361.85:      $1,568.09
AL tax:                    $1,678.09

AL withheld (Box 17):      $X,XXX.XX
AL refund/owed:            calculated
```

## AL Deductions and Credits

### Federal Tax Deduction
AL's most distinctive feature. Deducting federal tax from state income effectively reduces AL taxes by about 10-22% of the federal tax (depending on the AL bracket). This makes AL's effective rate lower than the 5% top bracket suggests.

### Standard Deduction + Personal Exemption
AL provides both a standard deduction ($3,000) and a personal exemption ($1,500). Combined with the federal tax deduction, the total deductions are substantial.

### Renter Benefit
AL does **not** offer a renter's credit or deduction.

### Earned Income Credit
- AL does **not** currently offer its own state EIC

### Student Loan Interest
AL does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

## Filing AL State Return

### Form 40
1. Go to https://www.revenue.alabama.gov/ (My Alabama Taxes)
2. Free e-filing available for AL residents
3. Enter federal AGI as starting point
4. Deduct federal income tax paid (Form 1040, Line 24)
5. Subtract standard deduction ($3,000) and personal exemption ($1,500)
6. Calculate tax from AL brackets
7. Enter withholding from Box 17
8. Calculate refund or amount owed

## What to Tell the User

> "Alabama has progressive brackets (2%-5%) but the top rate kicks in at just $3,001. The big perk: Alabama lets you deduct your federal income tax from your state taxable income, which lowers your AL bill significantly. After the federal tax deduction, standard deduction ($3,000), and personal exemption ($1,500), your AL taxable income is much lower than your AGI. File for free at revenue.alabama.gov."
