---
name: calculate
description: Calculate (or recalculate) the complete Form 1040 federal tax return line by line. Uses W-2 data and intake answers from a previous /ezfile:file-taxes session.
user-invocable: true
---

# Calculate Federal Tax Return

Compute the complete Form 1040 (or 1040-SR) for a single filer with W-2 income.

## Prerequisites

Before calculating, verify that return data exists:
1. Check `./returns/` for W-2 data (either from a prior `/ezfile:file-taxes` session or manually entered)
2. If no data exists, tell the user: "No W-2 data found. Run `/ezfile:file-taxes <path-to-w2>` first."

## Reference Files

Read these files before calculating:
- `reference/tax-year-2025.md` -- brackets, standard deduction, key constants
- `reference/schedule-1a-2025.md` -- Schedule 1-A deduction rules (if applicable)
- `reference/credits-2025.md` -- Saver's Credit and EIC rules

## The 10-Step Calculation Pipeline

### STEP 1: INCOME

```
Line 1a = Sum of W-2 Box 1 from all W-2s
Line 1z = Line 1a  (only W-2 income for this profile)
Line 9  = Line 1z  (total income = wages only)
```

### STEP 2: ADJUSTMENTS TO INCOME (Schedule 1)

Only student loan interest applies for this profile:

```
IF student_loan_interest > 0:
    raw = min(student_loan_interest, 2500)
    MAGI = Line 9  (total income, before adjustments)

    IF MAGI <= 85000:
        deduction = raw
    ELIF MAGI >= 100000:
        deduction = 0
    ELSE:
        deduction = raw * (1 - (MAGI - 85000) / 15000)
        deduction = round(deduction, 2)

    Schedule_1_Line_21 = deduction
    Schedule_1_Line_26 = deduction
    Line_10 = deduction
ELSE:
    Line_10 = 0
```

### STEP 3: ADJUSTED GROSS INCOME

```
Line 11 = Line 9 - Line 10
```

This is the AGI -- the most important number on the return. It determines eligibility for credits and deduction phaseouts.

### STEP 4: SCHEDULE 1-A DEDUCTIONS (New for 2025)

Calculate each applicable deduction with MAGI phaseout:

```
MAGI_for_1A = Line 11  (AGI)

# Phaseout function (shared by all Schedule 1-A deductions)
def apply_phaseout(amount, magi):
    if magi <= 75000: return amount
    if magi >= 100000: return 0
    return round(amount * (1 - (magi - 75000) / 25000), 2)

# Tip deduction (Line 1)
tip_deduction = apply_phaseout(tip_income, MAGI_for_1A)

# Overtime deduction (Line 2)
overtime_deduction = apply_phaseout(overtime_pay, MAGI_for_1A)

# Auto loan interest (Line 3) -- max $10,000
auto_loan_deduction = apply_phaseout(min(auto_loan_interest, 10000), MAGI_for_1A)

# Senior deduction (Line 4) -- only if age 65+
IF age >= 65:
    senior_1a_deduction = apply_phaseout(4000, MAGI_for_1A)
ELSE:
    senior_1a_deduction = 0

Schedule_1A_Line_5 = tip_deduction + overtime_deduction + auto_loan_deduction + senior_1a_deduction
Line_12c = Schedule_1A_Line_5
```

### STEP 5: STANDARD DEDUCTION

```
IF age >= 65:
    Line_12a = 17750  (single, 65+: $15,750 + $2,000 additional)
ELSE:
    Line_12a = 15750  (single, under 65)
```

### STEP 6: TOTAL DEDUCTIONS

```
Line_12b = 0  (no charitable deduction for this profile)
Line_13 = 0   (no QBI deduction for W-2 filers)
Line_14 = Line_12a + Line_12b + Line_12c + Line_13
```

### STEP 7: TAXABLE INCOME

```
Line_15 = max(Line_11 - Line_14, 0)
```

### STEP 8: TAX FROM BRACKETS

Apply 2025 single filer brackets:

```
taxable = Line_15

if taxable <= 11925:
    tax = taxable * 0.10
elif taxable <= 48475:
    tax = 1192.50 + (taxable - 11925) * 0.12
elif taxable <= 103350:
    tax = 5578.50 + (taxable - 48475) * 0.22
elif taxable <= 197300:
    tax = 17651.00 + (taxable - 103350) * 0.24
elif taxable <= 250525:
    tax = 40099.00 + (taxable - 197300) * 0.32
elif taxable <= 626350:
    tax = 57131.00 + (taxable - 250525) * 0.35
else:
    tax = 188769.75 + (taxable - 626350) * 0.37

Line_16 = round(tax, 2)
```

### STEP 9: CREDITS

**Saver's Credit (Form 8880) -- Nonrefundable:**

```
retirement_contributions = sum of W-2 Box 12 amounts for codes D, E, G, AA, BB
eligible_amount = min(retirement_contributions, 2000)

IF eligible_amount > 0:
    IF Line_11 <= 23750:
        credit_rate = 0.50
    ELIF Line_11 <= 25750:
        credit_rate = 0.20
    ELIF Line_11 <= 39500:
        credit_rate = 0.10
    ELSE:
        credit_rate = 0

    savers_credit = round(eligible_amount * credit_rate, 2)
    savers_credit = min(savers_credit, Line_16)  # Can't exceed tax
ELSE:
    savers_credit = 0

Line_19 = savers_credit
```

**Earned Income Credit -- Refundable:**

```
IF Line_11 < 19104 AND age >= 25 AND age <= 64:
    # Simplified EIC calculation (no qualifying children)
    earned_income = Line_1a

    IF earned_income <= 8490:
        eic = round(earned_income * 0.0765, 2)
    ELIF earned_income <= 10330:
        eic = 649  # Maximum
    ELSE:
        eic = max(round(649 - (earned_income - 10330) * 0.0765, 2), 0)

    # Also check against AGI
    IF Line_11 > 10330:
        agi_eic = max(round(649 - (Line_11 - 10330) * 0.0765, 2), 0)
        eic = min(eic, agi_eic)

    Line_27 = eic
ELSE:
    Line_27 = 0
```

**Total Tax:**

```
Line_22 = max(Line_16 - Line_19, 0)
Line_24 = Line_22  (no additional taxes for this profile)
```

### STEP 10: PAYMENTS & RESULT

```
Line_25a = Sum of W-2 Box 2 from all W-2s
Line_25d = Line_25a
Line_33 = Line_25d + Line_27  (withholding + refundable credits)

IF Line_33 > Line_24:
    Line_34 = Line_33 - Line_24  → REFUND
    Line_37 = 0
ELSE:
    Line_34 = 0
    Line_37 = Line_24 - Line_33  → AMOUNT OWED
```

## Verification

After computing, verify these invariants:
1. Line 11 = Line 9 - Line 10
2. Line 15 = max(Line 11 - Line 14, 0)
3. Line 15 >= 0
4. Line 16 >= 0
5. Line 22 = max(Line 16 - Line 19, 0)
6. Line 24 = Line 22
7. Line 33 = Line 25d + Line 27
8. Line 34 = max(Line 33 - Line 24, 0) OR Line 37 = max(Line 24 - Line 33, 0)
9. Line 34 and Line 37 cannot both be > 0

If any invariant fails, display the error and recompute.

## Output

### Save to Files

Write complete return to `./returns/return-2025.json`:
```json
{
  "tax_year": 2025,
  "filing_status": "single",
  "form": "1040",
  "line_1a": 0,
  "line_9": 0,
  "line_10": 0,
  "line_11": 0,
  "line_12a": 0,
  "line_12c": 0,
  "line_14": 0,
  "line_15": 0,
  "line_16": 0,
  "line_19": 0,
  "line_22": 0,
  "line_24": 0,
  "line_25a": 0,
  "line_27": 0,
  "line_33": 0,
  "line_34": 0,
  "line_37": 0,
  "schedules": {
    "schedule_1": { "line_21": 0, "line_26": 0 },
    "schedule_1a": { "line_1": 0, "line_2": 0, "line_3": 0, "line_4": 0, "line_5": 0 }
  }
}
```

### Display Summary

Show the full return summary using the format from the review skill.

### Suggest Next Steps

- Run `/ezfile:checklist` for filing instructions
- Run `/ezfile:explain <topic>` for explanations
- Run `/ezfile:review` to see the summary again
