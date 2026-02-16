---
name: checklist
description: Step-by-step guide to file your completed return at freefilefillableforms.com. Shows exactly which fields to fill and what values to enter.
user-invocable: true
---

# Filing Checklist for Free File Fillable Forms

Generate a complete, step-by-step guide for the user to file their return at freefilefillableforms.com.

## Prerequisites

Read `./returns/return-2025.json` for the calculated return data and `reference/form-1040-field-map.md` for field mapping details.

If no return data exists:
> "No return data found. Run `/ezfile:file-taxes <path-to-w2>` to calculate your return first."

## Part 1: Before You Start

Display this checklist:

```
BEFORE YOU START — Gather These Items

  [ ] Your W-2 (the original, not EZFile's summary)
  [ ] Your Social Security Number (you'll need the full number to file)
  [ ] Your date of birth
  [ ] Your current mailing address
  [ ] Last year's AGI (from your 2024 tax return, needed for identity verification)
      → If you didn't file last year, you'll need your prior year Self-Select PIN
      → If this is your first time filing, enter $0
  [ ] Bank account info for direct deposit (routing number + account number)
      → Check or savings account
      → This is optional but gets your refund 2-3 weeks faster
  [ ] 1098-E form (if claiming student loan interest deduction)
```

## Part 2: Create Your Account

```
STEP 1: Go to https://www.freefilefillableforms.com/

STEP 2: Click "Start Free File Fillable Forms"

STEP 3: Create an account
  - Enter your SSN, name, date of birth
  - Enter prior year AGI for identity verification
  - Create a username and password
  - SAVE these credentials -- you'll need them if you come back

STEP 4: Select your form
  → Form 1040 (if under 65)
  → Form 1040-SR (if 65 or older)
```

## Part 3: Fill In the Form

Read the return data and generate specific line-by-line instructions.

```
STEP 5: Personal Information (top of Form 1040)
  - First name and middle initial: [from W-2]
  - Last name: [from W-2]
  - Social Security Number: [enter your full SSN from your W-2]
  - Filing status: Check "Single"
  - Digital assets: Check "No" (unless you sold/traded cryptocurrency)

STEP 6: Address
  - Enter your CURRENT mailing address
  - (This may differ from the address on your W-2)

STEP 7: Income
  - Line 1a: Enter $[line_1a amount]
    (This is your wages from W-2 Box 1)
  - Line 1z: Enter $[line_1z amount] (same as 1a)
  - Line 9: Enter $[line_9 amount]
    (Total income — same as 1z for your situation)
```

### If Schedule 1 (Student Loan Interest):
```
STEP 7a: Add Schedule 1
  - Click "Add Form" → search "Schedule 1" → select it
  - Line 21: Enter $[schedule_1_line_21]
    (Your student loan interest deduction)
  - Line 26: Enter $[schedule_1_line_26]
    (Same as Line 21 for your situation)
  - Return to Form 1040
  - Line 10: Enter $[line_10]
    (This is Schedule 1, Line 26)
```

### Continue Form 1040:
```
STEP 8: AGI
  - Line 11: Enter $[line_11]
    (This is your Adjusted Gross Income: Line 9 minus Line 10)

STEP 9: Deductions
  - Line 12a: Enter $[line_12a]
    (Standard deduction: $15,750 or $17,750 if 65+)
  - Check the "You as a dependent" box: NO
  - Line 12b: Enter $0
```

### If Schedule 1-A deductions:
```
STEP 9a: Add Schedule 1-A
  - Click "Add Form" → search "Schedule 1-A" → select it
  - Line 1: Enter $[schedule_1a_line_1] (tip deduction)     [if applicable]
  - Line 2: Enter $[schedule_1a_line_2] (overtime deduction) [if applicable]
  - Line 3: Enter $[schedule_1a_line_3] (auto loan interest) [if applicable]
  - Line 4: Enter $[schedule_1a_line_4] (senior deduction)   [if applicable]
  - Line 5: Enter $[schedule_1a_line_5] (total)
  - Return to Form 1040
  - Line 12c: Enter $[line_12c]
    (This is Schedule 1-A, Line 5)
```

### Continue:
```
STEP 10: More Deductions
  - Line 13: Enter $0
    (Qualified business income — not applicable for W-2 filers)
  - Line 14: Enter $[line_14]
    (Total deductions: 12a + 12b + 12c + 13)

STEP 11: Taxable Income
  - Line 15: Enter $[line_15]
    (Line 11 minus Line 14, or $0 if negative)

STEP 12: Tax
  - Line 16: Enter $[line_16]
    (Tax from brackets — EZFile calculated this for you)

STEP 13: Credits
  - Line 17: Enter $0
  - Line 18: Enter $[line_16] (same as Line 16)
```

### If Saver's Credit:
```
STEP 13a: Add Form 8880 (Saver's Credit)
  - Click "Add Form" → search "8880" → select it
  - Fill in your retirement contribution amount and AGI
  - The credit flows to Schedule 3, Line 4
  - Then to Form 1040, Line 19

  - Line 19: Enter $[line_19]
```

### If no Saver's Credit:
```
  - Line 19: Enter $0
```

### Continue:
```
STEP 14: Total Tax
  - Line 22: Enter $[line_22]
    (Line 18 minus Line 19 — cannot be less than $0)
  - Line 23: Enter $0
  - Line 24: Enter $[line_24]
    (Total tax — this is what you actually owe the government)

STEP 15: Payments
  - Line 25a: Enter $[line_25a]
    (Federal tax withheld — from W-2 Box 2)
  - Line 25d: Enter $[line_25a]
    (Same as 25a for your situation)
  - Line 26: Enter $0
```

### If Earned Income Credit:
```
  - Line 27a: Enter $[line_27]
    (Earned Income Credit)
    Check the box for "nontaxable combat pay" only if applicable
```

### Continue:
```
STEP 16: Total Payments
  - Line 33: Enter $[line_33]
    (Line 25d + Line 27a)
```

### If Refund:
```
STEP 17: Your Refund!
  - Line 34: Enter $[line_34]
    (Line 33 minus Line 24 — this is your refund!)
  - Line 35a: Enter $[line_34]
    (Amount you want refunded)
  - Check "Direct deposit":
    - Line 35b: Enter your bank routing number (9 digits)
    - Line 35c: Select "Checking" or "Savings"
    - Line 35d: Enter your bank account number

  Direct deposit tip: Your routing and account numbers are
  on the bottom of your checks, or in your bank's mobile app
  under "account details."
```

### If Amount Owed:
```
STEP 17: Amount You Owe
  - Line 37: Enter $[line_37]
    (Line 24 minus Line 33 — this is what you owe)
  - You can pay online at https://www.irs.gov/payments
  - Due by April 15, 2026
```

## Part 4: Review and Submit

```
STEP 18: Review
  - Click "Review" or "Check for Errors"
  - Free File Fillable Forms will flag obvious issues
  - Double-check these key numbers against your W-2:
    □ Line 1a matches W-2 Box 1
    □ Line 25a matches W-2 Box 2
    □ Your SSN is correct
    □ Your name matches your Social Security card

STEP 19: Sign and Submit
  - Enter your occupation (your job title)
  - Enter your phone number
  - Enter your Identity Protection PIN (if you have one from the IRS)
  - E-sign the return
  - Click "Submit" or "File"

STEP 20: Confirmation
  - Save your confirmation number
  - Download or print a PDF copy of your filed return
  - Store it securely for at least 3 years (IRS audit window)
```

## Part 5: After Filing

```
AFTER YOU FILE:

  □ Save your confirmation number: _______________
  □ Download a PDF copy of your return
  □ Check refund status in ~24 hours at:
    https://www.irs.gov/refunds ("Where's My Refund?")
  □ Expected refund timeline:
    - E-file + direct deposit: ~21 days
    - E-file + paper check: ~4-6 weeks
  □ Keep your W-2 and return copy for 3 years minimum
  □ Delete or securely store the files in ./returns/
```

## Part 6: State Return

Based on the W-2 state:

**If no-income-tax state:**
> "Your state ([State]) has no income tax. No state return needed!"

**If PA:**
> "For Pennsylvania, file at https://www.revenue.pa.gov/ using myPATH. PA uses a simple flat 3.07% rate on your Box 16 wages."

**If NY:**
> "For New York, file at https://www.tax.ny.gov/ using NY Free File. NY starts from your federal AGI and applies its own brackets."

**If CA:**
> "For California, file at https://www.ftb.ca.gov/ using CalFile. Check if you qualify for the $60 renter's credit."

**Other states:**
> "For [State], check your state tax agency's website for free filing options. Many states offer free e-filing for simple returns."

## Disclaimer (Show at End)

> **Reminder:** EZFile calculated these numbers, but you are responsible for verifying them against your W-2 and entering them correctly. EZFile is not a tax preparer and does not file your return. For questions about your specific tax situation, consult a CPA or enrolled agent.
