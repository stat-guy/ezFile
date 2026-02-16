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

Based on the W-2 state, provide filing instructions. Read `reference/states/<st>.md` for detailed state rules.

**If no-income-tax state** (AK, FL, NV, NH, SD, TN, TX, WA, WY):
> "Your state ([State]) has no income tax. No state return needed!"

**If PA:**
> "For Pennsylvania, file at https://www.revenue.pa.gov/ using myPATH. PA uses a simple flat 3.07% rate on your Box 16 wages."

**If NY:**
> "For New York, file at https://www.tax.ny.gov/ using NY Free File. NY starts from your federal AGI and applies its own brackets."

**If CA:**
> "For California, file at https://www.ftb.ca.gov/ using CalFile. Check if you qualify for the $60 renter's credit."

**If CT:**
> "For Connecticut, file at https://portal.ct.gov/drs using myconneCT. CT has progressive brackets (2%-6.99%). Note: the personal exemption phases out above ~$44,500 AGI."

**If NJ:**
> "For New Jersey, file at https://www.nj.gov/treasury/taxation/ using NJ E-File. NJ uses its own income definition and progressive brackets (1.4%-10.75%). Renters: 18% of your rent counts as a property tax deduction."

**If IL:**
> "For Illinois, file at https://mytax.illinois.gov/. IL uses a flat 4.95% rate on federal AGI minus a $2,850 personal exemption."

**If WI:**
> "For Wisconsin, file at https://www.revenue.wi.gov/ using WI E-File. WI has progressive brackets (3.5%-7.65%) and a sliding-scale standard deduction. If household income is under $24,680, check Homestead Credit eligibility."

**If MA:**
> "For Massachusetts, file at https://www.mass.gov/masstaxconnect. MA uses a flat 5.00% rate with a $4,400 exemption. Renters: you can deduct 50% of rent paid, up to $4,000."

**If RI:**
> "For Rhode Island, file at https://www.tax.ri.gov/. RI has three brackets (3.75%-5.99%) and a $10,900 standard deduction."

**If ME:**
> "For Maine, file at https://www.maine.gov/revenue/ using Maine FastFile. ME has three brackets (5.8%-7.15%) and a $15,750 standard deduction. Renters with income under $40,000 may qualify for the Property Tax Fairness Credit (up to $1,000)."

**If IN:**
> "For Indiana, file at https://intime.dor.in.gov/. IN uses a flat 3.00% state rate plus mandatory county tax (varies by county). Renters can deduct up to $4,000 of rent paid."

**If CO:**
> "For Colorado, file at https://tax.colorado.gov/ using Revenue Online. CO uses a flat 4.40% rate on your federal taxable income (Line 15 -- after the standard deduction is already applied)."

**If AZ:**
> "For Arizona, file at https://azdor.gov/ using AZTaxes. AZ uses a flat 2.50% rate with a standard deduction that matches the federal amount ($15,750)."

**If UT:**
> "For Utah, file at https://tax.utah.gov/. UT uses a flat 4.50% rate on federal AGI. Instead of a standard deduction, UT gives you a Taxpayer Tax Credit."

**If MI:**
> "For Michigan, file at https://www.michigan.gov/taxes. MI uses a flat 4.25% rate with a $5,600 personal exemption. Renters: check if you qualify for the Homestead Property Tax Credit (20% of rent counts as property tax, credit up to $1,700)."

**If OH:**
> "For Ohio, file at https://myportal.tax.ohio.gov/ (OH|TAX). The first $26,050 of income is tax-free, then 2.75%/3.125%. Note: most Ohio cities also levy their own income tax (typically 2-2.5%) -- check W-2 Boxes 18-20."

**If KY:**
> "For Kentucky, file at https://mytaxes.ky.gov/ (KY File -- free for all residents). KY uses a flat 4.0% rate with a $3,270 standard deduction."

**If VA:**
> "For Virginia, file at https://www.tax.virginia.gov/. VA has progressive brackets (2%-5.75%) with an $8,000 standard deduction and $930 personal exemption. Important: Virginia's deadline is **May 1**, not April 15."

**If HI:**
> "For Hawaii, file at https://tax.hawaii.gov/. HI has 12 brackets (1.4%-11%) -- the most of any state. Standard deduction is very low ($2,200). Important: Hawaii's deadline is **April 20**."

**If WV:**
> "For West Virginia, file at https://mytaxes.wvtax.gov/. WV has progressive brackets (2.16%-4.67%) with a $2,000 personal exemption."

**If NC:**
> "For North Carolina, file via NC Free File at https://www.ncdor.gov/. NC uses a flat 4.25% rate with a $12,750 standard deduction."

**If SC:**
> "For South Carolina, file through approved e-file software at https://dor.sc.gov/. SC has three brackets (0%, 3%, 6%) with a $15,000 standard deduction. SC starts from your federal taxable income (Line 15)."

**If GA:**
> "For Georgia, file through Free File Alliance at https://dor.georgia.gov/. GA uses a flat 5.19% rate with a $12,000 standard deduction."

**If VT:**
> "For Vermont, file at https://tax.vermont.gov/ (myVTax). VT has progressive brackets (3.35%-8.75%) starting from your federal taxable income. Renters: file Form PR-141 separately for VT's Renter Rebate (up to ~$3,000)."

**If MD:**
> "For Maryland, file at https://www.marylandtaxes.gov/. MD has progressive brackets (2%-5.75%) plus a mandatory county tax (typically 3.20%). Standard deduction is 15% of AGI (capped at $2,550). Renters: apply separately for MD's Renter's Tax Credit."

**If DE:**
> "For Delaware, file at https://revenue.delaware.gov/. DE has progressive brackets (0%-6.60%) with a $3,250 standard deduction. Important: Delaware's deadline is **April 30**."

**If AL:**
> "For Alabama, file at https://www.revenue.alabama.gov/ (My Alabama Taxes). AL has brackets (2%-5%) with a unique perk: you can deduct your federal income tax from your AL taxable income."

**If MS:**
> "For Mississippi, file through approved e-file providers at https://www.dor.ms.gov/. MS taxes at 4.4% on income over $10,000 (first $10,000 tax-free). Standard deduction $2,300 + personal exemption $6,000. MS is phasing out its income tax by 2030."

**If MN:**
> "For Minnesota, file at https://www.revenue.state.mn.us/. MN has progressive brackets (5.35%-9.85%) starting from your federal taxable income. Very important for renters: file Form M1PR separately for MN's Renter's Property Tax Refund (up to ~$2,270) -- deadline is **August 15**."

**If IA:**
> "For Iowa, file via Free File Alliance at https://revenue.iowa.gov/. IA uses a flat 3.80% rate on your federal taxable income (Line 15). Important: Iowa's deadline is **April 30**."

**If MO:**
> "For Missouri, file via Free File Alliance at https://dor.mo.gov/. MO has narrow brackets with a top rate of 4.70% (kicks in at ~$9,192). Standard deduction matches federal ($15,750)."

**If AR:**
> "For Arkansas, file at https://atap.arkansas.gov/. AR has progressive brackets (0%-3.9%) with the first $5,499 tax-free, a $2,470 standard deduction, and a $29 personal credit."

**If LA:**
> "For Louisiana, file at https://latap.revenue.louisiana.gov/. LA completely reformed for 2025: flat 3.0% rate with a $12,500 standard deduction. Important: Louisiana's deadline is **May 15**."

**If ND:**
> "For North Dakota, file at https://www.tax.nd.gov/. ND's first $48,475 of taxable income is completely tax-free. At your income level, you likely owe NO ND tax."

**If NE:**
> "For Nebraska, file at https://revenue.nebraska.gov/ using NebFile. NE has progressive brackets (2.46%-5.20%) with an $8,600 standard deduction and $171 personal credit."

**If KS:**
> "For Kansas, file at https://www.kansas.gov/webfile/ or via IRS Direct File. KS has two brackets (5.20%/5.58%) with a $3,605 standard deduction and $9,160 personal exemption. Lower-income renters may qualify for a Homestead Refund."

**If OK:**
> "For Oklahoma, file at https://oktap.tax.ok.gov/. OK has a top rate of 4.75% with a $6,350 standard deduction."

**If MT:**
> "For Montana, file via Free File Alliance at https://revenue.mt.gov/. MT has two brackets (4.70%/5.90%) starting from your federal taxable income (Line 15). Montana has no sales tax."

**If NM:**
> "For New Mexico, file at https://tap.state.nm.us/ or via IRS Direct File. NM has progressive brackets (1.50%-5.90%). If your income is under $36,000, check the Low-Income Comprehensive Tax Rebate."

**If ID:**
> "For Idaho, file at https://tax.idaho.gov/ or via IRS Direct File. ID uses a flat 5.30% rate on your federal taxable income (Line 15). You also get a $120 grocery credit."

**If OR:**
> "For Oregon, file at https://www.oregon.gov/dor/ via Direct File Oregon. OR has high rates (4.75%-9.90%) but a federal tax subtraction (up to $7,650) and a $256 personal credit. Oregon has no sales tax."

**If DC:**
> "For D.C., file at https://otr.cfo.dc.gov/ (MyTax DC). DC has progressive brackets (4%-10.75%) with a $15,750 standard deduction. Renters: file Schedule H for a property tax credit (20% of rent, up to $1,425, AGI ≤ $66,000)."

**If PR:**
> "Puerto Rico has its own separate tax system. PR residents generally don't file federal Form 1040 for PR-source income. File your PR return at suri.hacienda.pr.gov or consult a CPA familiar with PR taxation."

**If VI:**
> "The U.S. Virgin Islands uses a 'mirror' of the federal tax code, filed with the USVI Bureau of Internal Revenue (not the IRS). File at vibir.gov or consult a USVI tax professional."

**Other states:**
> "For [State], check your state tax agency's website for free filing options. Many states offer free e-filing for simple returns."

## Disclaimer (Show at End)

> **Reminder:** EZFile calculated these numbers, but you are responsible for verifying them against your W-2 and entering them correctly. EZFile is not a tax preparer and does not file your return. For questions about your specific tax situation, consult a CPA or enrolled agent.
