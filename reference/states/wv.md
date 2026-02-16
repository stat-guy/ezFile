# West Virginia State Tax Reference

## Overview

West Virginia has a progressive income tax with 5 brackets. Rates have been declining in recent years through multiple legislative actions.

| Parameter | Value |
|---|---|
| Tax type | Progressive (5 brackets) |
| Form | IT-140 |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- WV starts from federal AGI |
| Standard deduction | **None** |
| Personal exemption | **$2,000** per exemption |
| Free file available | Yes, at https://mytaxes.wvtax.gov/ |

## WV Tax Brackets (2025)

| Taxable Income | Rate |
|---|---|
| $0 - $10,000 | 2.16% |
| $10,001 - $25,000 | 2.87% |
| $25,001 - $40,000 | 3.23% |
| $40,001 - $60,000 | 4.30% |
| Over $60,000 | 4.67% |

**For EZFile's target user:** The first 4 brackets (up to $60,000) are most relevant.

### Bracket Computation

```
if wv_taxable <= 10,000:
    wv_tax = wv_taxable * 0.0216
elif wv_taxable <= 25,000:
    wv_tax = 216.00 + (wv_taxable - 10,000) * 0.0287
elif wv_taxable <= 40,000:
    wv_tax = 646.50 + (wv_taxable - 25,000) * 0.0323
elif wv_taxable <= 60,000:
    wv_tax = 1,131.00 + (wv_taxable - 40,000) * 0.043
else:
    wv_tax = 1,991.00 + (wv_taxable - 60,000) * 0.0467
```

## How WV Tax Works

### Step 1: Start from Federal AGI
WV begins with federal AGI (Form 1040, Line 11). Schedule M provides additions and subtractions.

### Step 2: WV Adjustments
For W-2-only filers, WV AGI typically equals federal AGI.

### Step 3: Personal Exemption
- **$2,000** per exemption (single filer = 1 exemption)
- If claimed as a dependent on another return: $500

### Step 4: WV Taxable Income
```
WV_taxable = WV_AGI - personal_exemption ($2,000)
WV_taxable = max(WV_taxable, 0)
```

### Step 5: Apply Brackets
Use the bracket table above.

### Step 6: Compare to Withholding
```
WV_withheld = W-2 Box 17
WV_refund_or_owed = WV_withheld - WV_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
WV AGI:                $42,829.35
Personal exemption:    -$2,000.00
WV taxable income:     $40,829.35

WV tax calculation:
  2.16% on $10,000:       $216.00
  2.87% on $15,000:       $430.50
  3.23% on $15,000:       $484.50
  4.30% on $829.35:        $35.66
WV tax:                $1,166.66

WV withheld (Box 17):  $X,XXX.XX
WV refund/owed:        calculated
```

## WV Deductions and Credits

### No Standard Deduction
WV does NOT offer a standard deduction. Only the $2,000 personal exemption applies.

### Renter Benefit
WV does **not** offer a general renter's credit or deduction. A Homestead Exemption exists for age **65+ or disabled** only.

### Earned Income Credit
- WV does **not** currently offer its own state EIC

### Student Loan Interest
WV does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

### Low-Income Family Tax Credit
Available to very low-income filers. Not typically applicable to EZFile's target demographic.

## Filing WV State Return

### IT-140 Form
1. Go to https://mytaxes.wvtax.gov/ (MyTaxes -- free online portal)
2. Enter federal AGI as starting point
3. Subtract personal exemption ($2,000)
4. Calculate tax from WV brackets
5. Enter withholding from Box 17
6. Calculate refund or amount owed

## What to Tell the User

> "West Virginia has progressive brackets (2.16%-4.67%) that have been declining in recent years. WV doesn't offer a standard deduction -- just a $2,000 personal exemption. The rates are relatively moderate, especially at lower income levels. File for free at mytaxes.wvtax.gov."
