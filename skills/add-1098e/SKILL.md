---
name: add-1098e
description: Add or update student loan interest deduction from Form 1098-E. Accepts a dollar amount or path to a 1098-E document.
argument-hint: <amount|path-to-1098e>
user-invocable: true
---

# Add Student Loan Interest Deduction

The user wants to add a student loan interest deduction to their return. This is an above-the-line deduction (Schedule 1, Line 21) that reduces AGI -- it helps even with the standard deduction.

## Input

`$ARGUMENTS` -- either:
- A dollar amount (e.g., `1800` or `$1,800.00`)
- A path to a 1098-E PDF/image

## Step 1: Determine the Interest Amount

**If a dollar amount was provided:**
- Parse the number (strip `$`, commas, whitespace)
- Confirm: "You paid $X in student loan interest. Is that correct?"

**If a file path was provided:**
- Read the 1098-E document
- Extract Box 1: "Student Loan Interest Received by Lender"
- Display: "Your 1098-E shows $X in student loan interest paid. Is that correct?"

## Step 2: Check Eligibility

Read `reference/tax-year-2025.md` for the student loan interest deduction rules.

### Requirements (all must be true)
- Filing status is Single (always true for EZFile users)
- The interest was paid on a **qualified student loan**
- The user is not claimed as a dependent on someone else's return
- MAGI is below $100,000 (full deduction below $85,000)

### Calculate the Deduction

```
raw_deduction = min(interest_paid, 2500)  # Max deduction is $2,500

# Estimate MAGI (use total wages if return not yet calculated,
# or Line 11 AGI if return exists)
MAGI = estimated_or_calculated_AGI

if MAGI <= 85000:
    deduction = raw_deduction
elif MAGI >= 100000:
    deduction = 0
    # Inform user they're over the phaseout
else:
    reduction_ratio = (MAGI - 85000) / 15000
    deduction = round(raw_deduction * (1 - reduction_ratio), 2)
```

## Step 3: Show the Impact

If a return has already been calculated (check `./returns/return-2025.json`):

```
Student Loan Interest Deduction

  Interest paid:              $X,XXX.XX
  Maximum deduction:          $2,500.00
  Your deduction:             $X,XXX.XX  [after phaseout if applicable]
  [If phaseout applied: "Reduced from $X to $Y because your AGI of $Z
   is in the $85K-$100K phaseout range"]

  Impact on your return:
    Previous AGI:             $XX,XXX.XX
    New AGI:                  $XX,XXX.XX  (-$X,XXX.XX)
    Previous taxable income:  $XX,XXX.XX
    New taxable income:       $XX,XXX.XX  (-$X,XXX.XX)
    Previous tax:              $X,XXX.XX
    New tax:                   $X,XXX.XX  (-$XXX.XX)
    Previous refund:           $X,XXX.XX
    New refund:                $X,XXX.XX  (+$XXX.XX)
```

If no return has been calculated yet, just store the information:
```
Student loan interest of $X,XXX.XX recorded.
This will be applied when you run /ezfile:calculate or when
your return is calculated via /ezfile:file-taxes.
```

## Step 4: Recalculate

If a return already exists, automatically recalculate the full return by following the same 10-step pipeline from the calculate skill. Update `./returns/return-2025.json` and `./returns/summary-2025.md`.

## Educational Note

After showing the impact, explain:

> **Why this matters:** The student loan interest deduction is an "above-the-line" deduction, meaning it reduces your Adjusted Gross Income (AGI) directly. This is valuable because:
> 1. It reduces your taxable income even if you take the standard deduction
> 2. A lower AGI can help you qualify for other credits (like the Saver's Credit)
> 3. For every dollar of deduction, you save [their marginal rate]% in taxes
>
> At your income level, your marginal tax rate is [10% or 12%], so this $X deduction saves you approximately $Y in taxes.

## Where It Goes on the Return

- Schedule 1, Part II, Line 21: Student loan interest deduction
- Schedule 1, Line 26: Total adjustments to income
- Form 1040, Line 10: Adjustments to income (from Schedule 1, Line 26)
- Form 1040, Line 11: AGI = Line 9 - Line 10
