# Ohio State Tax Reference

## Overview

Ohio has a simplified progressive income tax where the first $26,050 of income is tax-free. Ohio also has widespread municipal/city income taxes similar to Pennsylvania's local taxes.

| Parameter | Value |
|---|---|
| Tax type | Progressive (3 brackets, first bracket is 0%) |
| Form | IT-1040 |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- OH starts from federal AGI |
| Standard deduction | **None** (0% bracket serves this purpose) |
| Personal exemption | **$1,900-$2,400** (income-based sliding scale) |
| Free file available | Yes, at https://myportal.tax.ohio.gov/ (OH|TAX) |

## OH Tax Brackets (All Filing Statuses, 2025)

| Taxable Income | Rate |
|---|---|
| $0 - $26,050 | 0.00% |
| $26,051 - $100,000 | 2.75% |
| Over $100,000 | 3.125% |

**Key insight:** The 0% bracket on the first $26,050 effectively acts as a large standard deduction. For most W-2 filers, the effective rate is quite low.

### Bracket Computation

```
if oh_taxable <= 26,050:
    oh_tax = 0
elif oh_taxable <= 100,000:
    oh_tax = (oh_taxable - 26,050) * 0.0275
else:
    oh_tax = 2,033.63 + (oh_taxable - 100,000) * 0.03125
```

## How OH Tax Works

### Step 1: Start from Federal AGI
OH begins with federal AGI (Form 1040, Line 11).

### Step 2: OH Adjustments
Ohio has additions and deductions. For W-2-only filers, OH AGI typically equals federal AGI.

### Step 3: Personal Exemption (Income-Based)

Ohio's personal exemption is on a sliding scale:

| Ohio AGI | Exemption per Person |
|---|---|
| $40,000 or less | $2,400 |
| $40,001 - $80,000 | $2,150 |
| Over $80,000 | $1,900 |

For a single filer, only 1 exemption applies.

### Step 4: OH Taxable Income
```
OH_taxable = OH_AGI - personal_exemption
OH_taxable = max(OH_taxable, 0)
```

### Step 5: Apply Brackets
Use the bracket table above.

### Step 6: Compare to Withholding
```
OH_withheld = W-2 Box 17
OH_refund_or_owed = OH_withheld - OH_tax
```

### Sample Calculation (Federal AGI of $42,829)

```
OH AGI:                $42,829.35
Personal exemption:    -$2,150.00 (AGI is in $40K-$80K range)
OH taxable income:     $40,679.35

OH tax calculation:
  0.00% on $26,050:        $0.00
  2.75% on $14,629.35:   $402.31
OH tax:                   $402.31

OH withheld (Box 17):   $X,XXX.XX
OH refund/owed:         calculated
```

## Municipal/City Income Tax (Important!)

Ohio has widespread **city/municipal income taxes** similar to Pennsylvania's local taxes. Most Ohio cities levy their own income tax.

### Common City Tax Rates
| City | Rate |
|---|---|
| Columbus | 2.50% |
| Cleveland | 2.50% |
| Cincinnati | 1.80% |
| Dayton | 2.50% |
| Toledo | 2.50% |
| Akron | 2.50% |

### How City Taxes Work
- Administered by RITA (Regional Income Tax Agency) or CCA (Central Collection Agency)
- Usually withheld by employer (check W-2 Box 18-20)
- Separate filing may be required with the city or RITA/CCA
- Credit usually given for taxes paid to work city if different from home city

## OH Deductions and Credits

### No Standard Deduction
OH does NOT offer a standard deduction. The 0% bracket on the first $26,050 serves a similar purpose.

### Renter Benefit
OH does **not** offer a general renter's credit or deduction. A Homestead Credit exists for age **65+ or disabled** only.

### Earned Income Credit
- OH does **not** currently offer its own state EIC

### Student Loan Interest
OH does **not** allow a separate student loan interest deduction -- it's already reflected in federal AGI.

## Filing OH State Return

### IT-1040 Form
1. Go to https://myportal.tax.ohio.gov/ (OH|TAX -- free for all OH residents)
2. Enter federal AGI as starting point
3. Subtract personal exemption ($1,900-$2,400 depending on income)
4. Apply brackets (0% on first $26,050, then 2.75% / 3.125%)
5. Enter withholding from Box 17
6. Calculate refund or amount owed
7. **Note:** May also need to file city/municipal return separately

## What to Tell the User

> "Ohio has low state income tax rates -- the first $26,050 is completely tax-free, then 2.75% on income up to $100,000. However, most Ohio cities levy their own income tax (typically 2-2.5%), which is often withheld by your employer (check W-2 Boxes 18-20). You may need to file a city return separately with RITA or CCA. File your state return for free at myportal.tax.ohio.gov."
