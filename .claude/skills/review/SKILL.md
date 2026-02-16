---
name: review
description: Display your completed 2025 tax return summary for review. Shows every line item with explanations.
user-invocable: true
---

# Review Your Tax Return

Display the completed return in a clear, plain-English format. The user should be able to verify every number before filing.

## Prerequisites

Check for return data in `./returns/return-2025.json`. If it doesn't exist:
> "No return data found. Run `/ezfile:file-taxes <path-to-w2>` to calculate your return first."

## Display Format

Read `./returns/return-2025.json` and display:

```
═══════════════════════════════════════════════════
  2025 FEDERAL TAX RETURN SUMMARY
  Filing Status: Single
  Form: 1040 [or 1040-SR if 65+]
═══════════════════════════════════════════════════

  INCOME
    Line 1a  Wages (W-2 Box 1):        $XX,XXX.XX
    Line 9   Total income:             $XX,XXX.XX

  ADJUSTMENTS TO INCOME
    Line 10  Student loan interest:     -$X,XXX.XX  ← Schedule 1
    Line 11  Adjusted Gross Income:    $XX,XXX.XX

  DEDUCTIONS
    Line 12a Standard deduction:       -$XX,XXX.XX
    Line 12c Schedule 1-A deductions:   -$X,XXX.XX  [if applicable]
    Line 14  Total deductions:         -$XX,XXX.XX
    Line 15  Taxable income:           $XX,XXX.XX

  TAX CALCULATION
    10% on first $11,925:               $1,192.50
    12% on next $XX,XXX.XX:             $X,XXX.XX
    [additional brackets if applicable]
    Line 16  Tax:                        $X,XXX.XX
    Line 19  Saver's Credit:              -$XXX.XX  [if applicable]
    Line 22  Tax after credits:          $X,XXX.XX
    Line 24  TOTAL TAX:                  $X,XXX.XX

  PAYMENTS
    Line 25a Federal tax withheld:       $X,XXX.XX
    Line 27  Earned Income Credit:         $XXX.XX  [if applicable]
    Line 33  TOTAL PAYMENTS:             $X,XXX.XX

  ─────────────────────────────────────────────────
  [If refund:]
    Line 34  YOUR REFUND:                $X,XXX.XX
    → Choose direct deposit for fastest refund (~21 days)

  [If amount owed:]
    Line 37  AMOUNT YOU OWE:             $X,XXX.XX
    → Due by April 15, 2026
  ─────────────────────────────────────────────────
```

## Schedule Details (if applicable)

### If Schedule 1 was used:
```
  SCHEDULE 1 — Adjustments to Income
    Line 21  Student loan interest:     $X,XXX.XX
    Line 26  Total adjustments:         $X,XXX.XX
    → Flows to Form 1040, Line 10
```

### If Schedule 1-A was used:
```
  SCHEDULE 1-A — Additional Deductions (New for 2025)
    Line 1   Tip income deduction:      $X,XXX.XX  [if applicable]
    Line 2   Overtime pay deduction:    $X,XXX.XX  [if applicable]
    Line 3   Auto loan interest:        $X,XXX.XX  [if applicable]
    Line 4   Senior deduction:          $X,XXX.XX  [if applicable]
    Line 5   Total:                     $X,XXX.XX
    → Flows to Form 1040, Line 12c
```

## State Tax Summary

If state tax data is available, show:

```
  STATE RETURN — [State Name]
    State wages (Box 16):              $XX,XXX.XX
    State tax owed:                     $X,XXX.XX
    State tax withheld (Box 17):        $X,XXX.XX
    State refund/owed:                    $XXX.XX
```

## Key Insights

After the summary, provide 2-3 personalized insights:

1. **Withholding analysis:** If refund > $1,000, mention: "Your employer withheld $X more than needed. That's $Y/month that could've been in your paycheck. Consider adjusting your W-4."

2. **Effective tax rate:** "Your effective federal tax rate is [total tax / total income × 100]%. This is your real tax rate -- lower than your marginal bracket of [bracket]%."

3. **Missed opportunities:** If Saver's Credit or EIC was close to qualifying, mention what would have changed.

## Next Steps

```
  NEXT STEPS:
  → /ezfile:checklist     Step-by-step guide to file at freefilefillableforms.com
  → /ezfile:explain AGI   Understand what any number means
  → /ezfile:add-1098e     Add student loan interest (if not already added)
```

## Disclaimer

End with:
> **Reminder:** EZFile is a calculation assistant. Review all numbers against your W-2 before filing. You are responsible for the accuracy of your return.
