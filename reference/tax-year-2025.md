# 2025 Federal Tax Reference -- Single Filer

This file contains all tax constants for the 2025 tax year, scoped to single filers with no dependents.

## Filing Status

Always **Single**. This plugin does not support MFJ, MFS, HoH, or QSS.

## Standard Deduction

| Situation | Amount |
|---|---|
| Single, under 65 | **$15,750** |
| Single, 65 or older | **$17,750** ($15,750 + $2,000 additional) |
| Single, blind | **$17,750** ($15,750 + $2,000 additional) |
| Single, 65+ AND blind | **$19,750** ($15,750 + $2,000 + $2,000) |

The "65 or older" threshold for 2025: born before January 2, 1961.

## Federal Income Tax Brackets (Single)

| Taxable Income | Rate | Cumulative Tax at Top |
|---|---|---|
| $0 - $11,925 | 10% | $1,192.50 |
| $11,926 - $48,475 | 12% | $5,578.50 |
| $48,476 - $103,350 | 22% | $12,651.00 |
| $103,351 - $197,300 | 24% | $23,199.00 |
| $197,301 - $250,525 | 32% | $40,231.00 |
| $250,526 - $626,350 | 35% | $171,520.75 |
| Over $626,350 | 37% | -- |

### Bracket Computation (Single)

```
if taxable_income <= 11,925:
    tax = taxable_income * 0.10
elif taxable_income <= 48,475:
    tax = 1,192.50 + (taxable_income - 11,925) * 0.12
elif taxable_income <= 103,350:
    tax = 5,578.50 + (taxable_income - 48,475) * 0.22
elif taxable_income <= 197,300:
    tax = 17,651.00 + (taxable_income - 103,350) * 0.24
elif taxable_income <= 250,525:
    tax = 40,099.00 + (taxable_income - 197,300) * 0.32
elif taxable_income <= 626,350:
    tax = 57,131.00 + (taxable_income - 250,525) * 0.35
else:
    tax = 188,769.75 + (taxable_income - 626,350) * 0.37
```

Note: For this plugin's target demographic (W-2 single filers), the first 3-4 brackets are the only ones that matter.

## Social Security & Medicare

| Item | Rate | Wage Base |
|---|---|---|
| Social Security (employee share) | 6.2% | $176,100 |
| Medicare (employee share) | 1.45% | No limit |
| Additional Medicare (over $200K) | 0.9% | Over $200,000 |

## Student Loan Interest Deduction

| Parameter | Value |
|---|---|
| Maximum deduction | $2,500 |
| Phaseout start (Single) | $85,000 MAGI |
| Phaseout end (Single) | $100,000 MAGI |
| Phaseout range | $15,000 |
| Form line | Schedule 1, Part II, Line 21 |

### Phaseout Formula

```
if MAGI <= 85,000:
    deduction = min(interest_paid, 2500)
elif MAGI >= 100,000:
    deduction = 0
else:
    ratio = (MAGI - 85,000) / 15,000
    deduction = min(interest_paid, 2500) * (1 - ratio)
    deduction = round(deduction, 2)
```

## Form 1040 vs. Form 1040-SR

| Form | Who Uses It |
|---|---|
| Form 1040 | Filers under 65 |
| Form 1040-SR | Filers 65 or older (born before Jan 2, 1961) |

Both forms have identical line numbers and calculations. Form 1040-SR has larger print and a standard deduction chart on the form itself.

## Key Line Numbers (Form 1040)

| Line | Description | Source |
|---|---|---|
| 1a | Wages, salaries, tips | W-2 Box 1 (sum of all W-2s) |
| 8 | Other income from Schedule 1 | Schedule 1, Line 10 (if applicable) |
| 9 | Total income | Line 1a + Line 8 |
| 10 | Adjustments from Schedule 1 | Schedule 1, Line 26 |
| 11 | Adjusted Gross Income (AGI) | Line 9 - Line 10 |
| 12a | Standard deduction amount | $15,750 or $17,750 |
| 12b | Charitable (if not itemizing) | Usually $0 for this profile |
| 12c | Schedule 1-A deductions | New for 2025 (tips, overtime, etc.) |
| 13 | Qualified business income deduction | $0 for W-2 filers |
| 14 | Total deductions | Line 12a + 12b + 12c + 13 |
| 15 | Taxable income | max(Line 11 - Line 14, 0) |
| 16 | Tax | From brackets above |
| 19 | Nonrefundable credits | Saver's Credit if eligible |
| 22 | Amount of Line 16 minus credits | Line 16 - Line 19 |
| 24 | Total tax | Line 22 (for this profile) |
| 25a | Federal tax withheld (W-2s) | W-2 Box 2 (sum of all W-2s) |
| 25d | Total federal tax withheld | Line 25a (for this profile) |
| 27 | Earned Income Credit | If eligible |
| 33 | Total payments | Line 25d + Line 27 |
| 34 | Overpaid (if Line 33 > Line 24) | Line 33 - Line 24 = REFUND |
| 37 | Amount you owe (if Line 24 > Line 33) | Line 24 - Line 33 = OWED |

## CRITICAL: Do Not Double-Count

These W-2 Box 12 amounts are ALREADY excluded from Box 1:
- Code D: 401(k) contributions
- Code E: 403(b) contributions
- Code G: 457(b) contributions
- Code W: HSA employer contributions
- Code AA: Roth 401(k) contributions
- Code BB: Roth 403(b) contributions
- Code DD: Health insurance cost (informational only)

Do NOT subtract these again. They are shown on the W-2 for information only.
