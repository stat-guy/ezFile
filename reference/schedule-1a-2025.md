# Schedule 1-A: Additional Deductions (New for 2025)

Schedule 1-A is a **new schedule for the 2025 tax year** that provides above-the-line deductions for specific types of income and expenses. These deductions reduce AGI, meaning taxpayers benefit even when taking the standard deduction.

## Overview

Schedule 1-A deductions flow to Form 1040, Line 12c, which is added to the standard deduction on Line 12a to produce Line 14 (Total Deductions).

**Important:** These are NOT itemized deductions. They are additional above-the-line deductions available to ALL filers regardless of whether they itemize.

## Deduction Categories

### 1. Tip Income Deduction

| Parameter | Value |
|---|---|
| What qualifies | Cash and credit card tips reported as income |
| Maximum deduction | 100% of reported tip income |
| MAGI phaseout start (Single) | $75,000 |
| MAGI phaseout end (Single) | $100,000 |
| Where on W-2 | Tips are included in Box 1; Box 7 shows Social Security tips; Box 8 shows allocated tips |
| Schedule 1-A line | Line 1 |

**Who benefits:** Restaurant workers, bartenders, hotel staff, valets, hairdressers -- anyone who receives tips as part of their compensation.

**How it works:** If you earned tips that were included in your W-2 Box 1 wages, you can deduct them on Schedule 1-A. This effectively makes tip income tax-free (up to the phaseout threshold).

**Intake question:** "Did you receive tips at work in 2025?"

### 2. Overtime Pay Deduction

| Parameter | Value |
|---|---|
| What qualifies | Overtime pay (hours worked beyond 40/week at 1.5x rate) |
| Maximum deduction | 100% of overtime pay received |
| MAGI phaseout start (Single) | $75,000 |
| MAGI phaseout end (Single) | $100,000 |
| Where on W-2 | Included in Box 1; employer may detail in Box 14 |
| Schedule 1-A line | Line 2 |

**Who benefits:** Hourly workers who regularly work overtime -- factory workers, nurses, retail workers during holidays, etc.

**How it works:** If your employer paid you overtime wages (typically noted in your pay stubs or Box 14), you can deduct that amount. This effectively eliminates federal income tax on overtime pay.

**Intake question:** "Did you work overtime (paid at 1.5x your regular rate) in 2025? If yes, what was your total overtime pay?"

### 3. Auto Loan Interest Deduction

| Parameter | Value |
|---|---|
| What qualifies | Interest on a car loan for a vehicle purchased NEW in 2025 |
| Maximum deduction | $10,000 per year |
| MAGI phaseout start (Single) | $75,000 |
| MAGI phaseout end (Single) | $100,000 |
| Eligible vehicles | New vehicles only (not used); must be purchased in 2025 |
| Schedule 1-A line | Line 3 |

**Who benefits:** Anyone who bought a brand-new car in 2025 and is making payments with interest.

**How it works:** Interest paid on a new car loan is deductible up to $10,000. The vehicle must be new (not used) and purchased during the 2025 tax year.

**Intake question:** "Did you buy a brand-new car in 2025? If yes, how much auto loan interest did you pay?"

**Note:** This plugin's target user "doesn't own a car," but some users in the demographic may have purchased one during 2025. Ask the question anyway.

### 4. Senior Standard Deduction Enhancement

| Parameter | Value |
|---|---|
| What qualifies | Filers age 65 or older as of Dec 31, 2025 |
| Additional deduction | $4,000 |
| MAGI phaseout start (Single) | $75,000 |
| MAGI phaseout end (Single) | $100,000 |
| Schedule 1-A line | Line 4 |

**Who benefits:** Single filers born before January 2, 1961.

**How it works:** This is an additional deduction on top of the regular standard deduction enhancement for seniors. A qualifying senior gets:
- Regular standard deduction: $15,750
- Additional standard deduction for 65+: $2,000 (built into the $17,750)
- Schedule 1-A senior deduction: $4,000 (with phaseout)

**Note:** The regular additional standard deduction ($2,000) has NO phaseout. The Schedule 1-A senior deduction ($4,000) DOES phase out at $75K-$100K MAGI.

## MAGI Phaseout Calculation

All Schedule 1-A deductions share the same phaseout thresholds:

```
if MAGI <= 75,000:
    allowed = full_deduction_amount
elif MAGI >= 100,000:
    allowed = 0
else:
    ratio = (MAGI - 75,000) / 25,000
    allowed = full_deduction_amount * (1 - ratio)
    allowed = round(allowed, 2)
```

**Important MAGI note:** For Schedule 1-A phaseout purposes, MAGI is calculated BEFORE applying Schedule 1-A deductions but AFTER other above-the-line adjustments (like student loan interest from Schedule 1).

## How Schedule 1-A Flows to Form 1040

```
Schedule 1-A:
  Line 1: Tip income deduction
  Line 2: Overtime pay deduction
  Line 3: Auto loan interest deduction
  Line 4: Senior deduction
  Line 5: Total Schedule 1-A deductions (sum of Lines 1-4)

Form 1040:
  Line 12a: Standard deduction ($15,750 or $17,750)
  Line 12b: Charitable deduction (if not itemizing, usually $0)
  Line 12c: Schedule 1-A deductions (Line 5 from Schedule 1-A)
  Line 14: Total deductions = 12a + 12b + 12c + 13
```

## Interaction with Other Deductions

- Schedule 1-A deductions are **in addition to** the standard deduction
- They are **in addition to** Schedule 1 adjustments (student loan interest)
- They do NOT affect FICA taxes (Social Security and Medicare)
- They DO reduce federal income tax liability
- State treatment varies -- check individual state rules

## Documentation Requirements

For each Schedule 1-A deduction claimed, the taxpayer should retain:
- **Tips:** Pay stubs showing tip income, tip log if self-reported
- **Overtime:** Pay stubs showing overtime hours and pay rate
- **Auto loan interest:** Form 1098 from lender or year-end loan statement; purchase agreement showing vehicle is new
- **Senior deduction:** No additional documentation beyond DOB (already on return)
