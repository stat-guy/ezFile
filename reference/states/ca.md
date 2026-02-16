# California State Tax Reference

## Overview

California has the highest top marginal tax rate in the country and a progressive bracket system with many brackets.

| Parameter | Value |
|---|---|
| Tax type | Progressive (graduated brackets) |
| Form | 540 (resident) |
| Filing deadline | April 15 |
| Follows federal AGI? | **Yes** -- CA starts from federal AGI with modifications |
| Standard deduction (Single) | **$5,540** (2025 estimated) |
| Personal exemption credit | **$144** (single, 2025 estimated) |
| Free file available | Yes, CalFile at https://www.ftb.ca.gov/ |

## CA Tax Brackets (Single, 2025 Estimated)

| Taxable Income | Rate |
|---|---|
| $0 - $10,756 | 1.00% |
| $10,757 - $25,499 | 2.00% |
| $25,500 - $40,245 | 4.00% |
| $40,246 - $55,866 | 6.00% |
| $55,867 - $70,612 | 8.00% |
| $70,613 - $360,659 | 9.30% |
| $360,660 - $432,787 | 10.30% |
| $432,788 - $721,314 | 11.30% |
| Over $721,314 | 12.30% |

**Mental Disability Insurance (SDI):** 1.2% on all wages (automatically withheld; shown in W-2 Box 14 or Box 19).

**For EZFile's target user:** The first 5-6 brackets are most relevant.

### Bracket Computation (Single)

```
if ca_taxable <= 10,756:
    ca_tax = ca_taxable * 0.01
elif ca_taxable <= 25,499:
    ca_tax = 107.56 + (ca_taxable - 10,756) * 0.02
elif ca_taxable <= 40,245:
    ca_tax = 402.42 + (ca_taxable - 25,499) * 0.04
elif ca_taxable <= 55,866:
    ca_tax = 992.26 + (ca_taxable - 40,245) * 0.06
elif ca_taxable <= 70,612:
    ca_tax = 1,929.52 + (ca_taxable - 55,866) * 0.08
elif ca_taxable <= 360,659:
    ca_tax = 3,109.20 + (ca_taxable - 70,612) * 0.093
else:
    # Higher brackets exist but unlikely for this profile
    ca_tax = 30,083.57 + (ca_taxable - 360,659) * 0.103
```

## Calculation

### Step 1: Start from Federal AGI
CA begins with the federal AGI (Form 1040, Line 11).

### Step 2: CA Adjustments
CA has several differences from federal:
- **Student loan interest:** CA conforms to the federal deduction (already in federal AGI)
- **Schedule 1-A:** CA may NOT conform to new 2025 federal Schedule 1-A deductions. Check CA conformity legislation.

For this profile, CA AGI typically equals federal AGI.

### Step 3: CA Standard Deduction
- Single: **$5,540** (2025 estimated)
- This is significantly lower than the federal standard deduction

### Step 4: CA Taxable Income
```
CA_taxable = CA_AGI - CA_standard_deduction
CA_taxable = max(CA_taxable, 0)
```

### Step 5: Apply Brackets
Use the bracket table above.

### Step 6: Exemption Credit
- Single: $144 personal exemption credit (subtracted from tax, not income)

### Step 7: Final CA Tax
```
CA_tax = bracket_tax - exemption_credit
CA_tax = max(CA_tax, 0)
```

### Step 8: Compare to Withholding
```
CA_withheld = W-2 Box 17
CA_refund_or_owed = CA_withheld - CA_tax
```

## SDI (State Disability Insurance)

- Rate: 1.2% on all wages (2025)
- This is NOT an income tax -- it's a payroll tax
- Usually shown in W-2 Box 14 (code "SDI" or "CASDI") or Box 19
- The user cannot get this back (it's not a withholding against tax owed)
- Do NOT include SDI in the state income tax calculation

## Sample Calculation (Federal AGI of $42,829)

```
CA AGI:                $42,829.35
CA standard deduction: -$5,540.00
CA taxable income:     $37,289.35

CA tax calculation:
  1.00% on $10,756:       $107.56
  2.00% on $14,743:       $294.86
  4.00% on $11,790.35:    $471.61
CA gross tax:              $874.03
Exemption credit:         -$144.00
CA net tax:                $730.03

CA withheld (Box 17):    $X,XXX.XX
CA refund/owed:          calculated
```

## Key CA-Specific Items

### Renter's Credit
- Available to CA renters with AGI under $50,746 (single, 2025 estimated)
- Credit amount: **$60** (single)
- Must have paid rent for at least 6 months in CA
- **This applies to EZFile's target user!** Always check.

### CA Earned Income Tax Credit (CalEITC)
- CA has its own EIC for very low-income workers
- Income limit: ~$30,950 (2025 estimated)
- More generous than federal EIC for low earners
- If federal EIC applies, check CalEITC too

### Young Child Tax Credit
- Not applicable (no children)

## CA Conformity Notes

California often delays conforming to federal tax changes. For 2025:
- **Standard deduction:** CA uses its own ($5,540), not federal
- **Student loan interest:** CA conforms to federal treatment
- **Schedule 1-A deductions:** CA conformity is uncertain for 2025. Assume CA does NOT conform unless confirmed.

## Filing CA State Return

### Form 540
1. Go to CalFile: https://www.ftb.ca.gov/
2. Free for CA residents with qualifying income
3. Enter federal AGI as starting point
4. Apply CA standard deduction ($5,540)
5. Calculate tax from CA brackets
6. Subtract exemption credit ($144)
7. Enter withholding from Box 17
8. Calculate refund or amount owed
9. Check renter's credit eligibility

## What to Tell the User

> "California has its own tax brackets and a smaller standard deduction ($5,540 vs. the federal $15,750), so your CA taxable income will be higher. CA also has a renter's credit ($60) that you may qualify for. Good news: CA offers free filing through CalFile at ftb.ca.gov."
