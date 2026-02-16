# Form 1040 Field Map for Free File Fillable Forms

This document maps every Form 1040 line that EZFile calculates to the corresponding field on [Free File Fillable Forms](https://www.freefilefillableforms.com/).

## How Free File Fillable Forms Works

1. Go to https://www.freefilefillableforms.com/
2. Create an account (you'll need: SSN, DOB, prior year AGI or prior year self-select PIN)
3. Select "Form 1040" (or "Form 1040-SR" for seniors)
4. Fill in fields by clicking on them and typing values
5. Some fields auto-calculate; others you must enter manually
6. Add schedules (Schedule 1, Schedule 1-A) if needed
7. Review, e-sign, and submit

**Important:** Free File Fillable Forms does very little math for you. You must calculate most values yourself and enter them. That's exactly what EZFile does.

## Top Section: Personal Information

| Field | What to Enter | Source |
|---|---|---|
| Your first name and middle initial | Your legal name | W-2 Box e |
| Last name | Your legal last name | W-2 Box e |
| Your social security number | Your full SSN | W-2 Box a (you have the original document) |
| Filing status | Check "Single" | Always Single for EZFile users |
| Digital assets question | Check "No" (unless you had crypto) | Ask user if uncertain |

**Note:** Unlike EZFile, you WILL enter your full SSN on the actual tax form. EZFile masks it for privacy during calculation, but you need the real number to file.

## Address Section

| Field | What to Enter | Source |
|---|---|---|
| Home address | Your current mailing address | May differ from W-2 Box f |
| City, state, ZIP | Current city, state, ZIP | -- |

## Income Section

| 1040 Line | Field Name on Form | Value to Enter | Source |
|---|---|---|---|
| Line 1a | Wages, salaries, tips | [W-2 Box 1 total] | Sum of all W-2 Box 1 amounts |
| Line 1z | Add lines 1a through 1h | Same as Line 1a | For this profile, only 1a applies |
| Line 9 | Total income | Line 1z + Line 8 | Line 8 from Schedule 1 if applicable |

## Adjustments Section

| 1040 Line | Field Name on Form | Value to Enter | Source |
|---|---|---|---|
| Line 10 | Adjustments to income | [Schedule 1, Line 26] | Student loan interest deduction |
| Line 11 | Adjusted gross income | Line 9 - Line 10 | This is your AGI |

## Deductions Section

| 1040 Line | Field Name on Form | Value to Enter | Source |
|---|---|---|---|
| Line 12a | Standard deduction or itemized | $15,750 (under 65) or $17,750 (65+) | Check "You as a dependent" = NO |
| Line 12b | Charitable deduction | $0 | Not itemizing |
| Line 12c | Add Schedule 1-A | [Schedule 1-A total] | If tips/overtime/car loan/senior deduction |
| Line 13 | Qualified business income | $0 | W-2 only, no QBI |
| Line 14 | Total deductions | 12a + 12b + 12c + 13 | Sum of deductions |
| Line 15 | Taxable income | Line 11 - Line 14 | Cannot be negative (use $0 if negative) |

## Tax Section

| 1040 Line | Field Name on Form | Value to Enter | Source |
|---|---|---|---|
| Line 16 | Tax | [calculated from brackets] | Apply single tax brackets to Line 15 |
| Line 17 | Amount from Schedule 2, line 21 | $0 | No AMT or excess premium tax credit |
| Line 18 | Add lines 16 and 17 | Same as Line 16 | -- |
| Line 19 | Nonrefundable credits | [Saver's Credit if eligible] | From Schedule 3 |
| Line 21 | Other credits from Schedule 3 | $0 | -- |
| Line 22 | Subtract Line 19 from Line 18 | Line 18 - Line 19 | Cannot go below $0 |
| Line 23 | Other taxes from Schedule 2 | $0 | No additional taxes for this profile |
| Line 24 | Total tax | Line 22 + Line 23 | This is your total federal tax |

## Payments Section

| 1040 Line | Field Name on Form | Value to Enter | Source |
|---|---|---|---|
| Line 25a | Federal tax withheld from W-2s | [W-2 Box 2 total] | Sum of all W-2 Box 2 amounts |
| Line 25b | Federal tax withheld from 1099s | $0 | No 1099s |
| Line 25c | Other withholding | $0 | -- |
| Line 25d | Total federal tax withheld | Same as Line 25a | -- |
| Line 26 | Estimated tax payments | $0 | -- |
| Line 27a | Earned income credit | [EIC if eligible] | Check box if claiming; enter amount |
| Line 33 | Total other payments and credits | Line 25d + Line 27a | Total payments |

## Refund Section

| 1040 Line | Field Name on Form | Value to Enter | Source |
|---|---|---|---|
| Line 34 | Overpaid | Line 33 - Line 24 | Only if Line 33 > Line 24 |
| Line 35a | Refunded to you | Same as Line 34 | Check if you want direct deposit |
| Line 35b | Routing number | Your bank routing number | For direct deposit |
| Line 35c | Account type | Checking or Savings | For direct deposit |
| Line 35d | Account number | Your bank account number | For direct deposit |

## Amount You Owe Section

| 1040 Line | Field Name on Form | Value to Enter | Source |
|---|---|---|---|
| Line 37 | Amount you owe | Line 24 - Line 33 | Only if Line 24 > Line 33 |
| Line 38 | Estimated tax penalty | Usually $0 | May apply if owed > $1,000 |

## Schedule 1 (If Student Loan Interest)

Only needed if you have a student loan interest deduction.

### Adding Schedule 1 in Free File Fillable Forms:
1. Click "Add Form" or "+" button
2. Search for "Schedule 1"
3. Select "Schedule 1 (Form 1040)"

### Fields to Fill:

| Schedule 1 Line | Field Name | Value to Enter | Source |
|---|---|---|---|
| Line 21 | Student loan interest deduction | [deduction amount] | min(interest paid, $2,500) with phaseout |
| Line 26 | Total adjustments | Same as Line 21 | For this profile, only Line 21 applies |

**Flow:** Schedule 1 Line 26 → Form 1040 Line 10

## Schedule 1-A (If Tips/Overtime/Car/Senior Deduction)

Only needed if any Schedule 1-A deductions apply.

### Adding Schedule 1-A in Free File Fillable Forms:
1. Click "Add Form" or "+" button
2. Search for "Schedule 1-A"
3. Select "Schedule 1-A (Form 1040)"

### Fields to Fill:

| Schedule 1-A Line | Field Name | Value to Enter | Source |
|---|---|---|---|
| Line 1 | Tip income deduction | [tip amount with phaseout] | Tips from W-2, subject to MAGI phaseout |
| Line 2 | Overtime pay deduction | [overtime amount with phaseout] | Overtime pay, subject to MAGI phaseout |
| Line 3 | Auto loan interest | [interest with phaseout] | New car loan interest, max $10,000, subject to phaseout |
| Line 4 | Senior deduction | [deduction with phaseout] | $4,000 for 65+, subject to MAGI phaseout |
| Line 5 | Total | Sum of Lines 1-4 | Total Schedule 1-A deductions |

**Flow:** Schedule 1-A Line 5 → Form 1040 Line 12c

## Form 8880 (If Saver's Credit)

Only needed if AGI ≤ $39,500 and retirement contributions exist.

### Adding Form 8880 in Free File Fillable Forms:
1. Click "Add Form"
2. Search for "8880"
3. Select "Form 8880"

### Key Fields:

| Line | Value to Enter | Source |
|---|---|---|
| Line 1 | Retirement contributions | W-2 Box 12 (codes D, E, G, AA, BB) |
| Line 2 | $2,000 | Maximum eligible amount |
| Line 3 | min(Line 1, Line 2) | Smaller of contributions or $2,000 |
| Line 4 | Credit rate (50%, 20%, or 10%) | Based on AGI thresholds |
| Line 5 | Line 3 x Line 4 | Credit amount |

**Flow:** Form 8880 → Schedule 3 Line 4 → Form 1040 Line 19

## Signature Section

| Field | What to Enter |
|---|---|
| Your signature | E-sign with Free File Fillable Forms |
| Date | Date you file |
| Occupation | Your job title |
| Identity Protection PIN | If you received one from IRS (optional) |
| Phone number | Your phone number |

## After Submission

1. Free File Fillable Forms will provide a confirmation number
2. You can check your refund status at https://www.irs.gov/refunds ("Where's My Refund?")
3. E-filed returns with direct deposit: refund typically arrives in ~21 days
4. Save a PDF copy of your filed return for your records
