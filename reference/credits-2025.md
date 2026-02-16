# Tax Credits Reference -- 2025 (Single, No Dependents)

This file covers credits available to EZFile's target user: single, no children, W-2 income only.

## Credits Overview

Credits directly reduce your tax bill (unlike deductions, which reduce taxable income). A $200 credit saves you exactly $200.

There are two types:
- **Nonrefundable credits:** Can reduce your tax to $0 but not below. Cannot generate a refund on their own.
- **Refundable credits:** Can reduce your tax below $0, giving you money back even if you owe no tax.

## 1. Saver's Credit (Form 8880) -- Nonrefundable

The Retirement Savings Contributions Credit rewards low- and moderate-income taxpayers for contributing to retirement accounts.

### Eligibility Requirements (ALL must be met)
- Age 18 or older at end of 2025
- Not a full-time student (enrolled full-time for 5+ months)
- Not claimed as a dependent on someone else's return
- Made eligible retirement contributions (W-2 Box 12 codes D, E, G, AA, BB, or personal IRA contributions)

### 2025 AGI Thresholds (Single)

| AGI Range | Credit Rate | Max Credit (on $2,000) |
|---|---|---|
| $0 - $23,750 | 50% | $1,000 |
| $23,751 - $25,750 | 20% | $400 |
| $25,751 - $39,500 | 10% | $200 |
| Over $39,500 | 0% | $0 |

### Calculation

```
eligible_contributions = sum of W-2 Box 12 codes D, E, G, AA, BB
                         (plus any personal IRA contributions, but rare for this profile)
base = min(eligible_contributions, 2000)

if AGI <= 23,750:
    credit = base * 0.50
elif AGI <= 25,750:
    credit = base * 0.20
elif AGI <= 39,500:
    credit = base * 0.10
else:
    credit = 0

# Credit cannot exceed the tax liability (nonrefundable)
credit = min(credit, tax_from_line_16)
```

### Where It Goes on Form 1040
- Calculated on Form 8880
- Flows to Schedule 3, Line 4
- Then to Form 1040, Line 20 (nonrefundable credits)

### EZFile Note
Most of this plugin's target users will have AGI above $39,500, making them ineligible. But lower-income filers (part-time workers, those who started mid-year) may qualify. Always check.

## 2. Earned Income Credit (EIC) -- Refundable

The EIC is a refundable credit for low-income workers. Without qualifying children, the credit is small but still valuable.

### Eligibility Requirements (ALL must be met for Single, No Children)
- Age 25-64 at end of 2025 (born after Dec 31, 1960 and before Jan 1, 2001)
- Not a dependent on someone else's return
- Not a qualifying child of another taxpayer
- Lived in the US for more than half the year
- Investment income must be $11,600 or less
- Must have earned income (W-2 wages count)
- Must not be filing Form 2555 (foreign earned income)

### 2025 Parameters (Single, No Qualifying Children)

| Parameter | Value |
|---|---|
| Maximum credit | $649 |
| Earned income amount for max credit | $8,490 |
| Phaseout begins at earned income | $10,330 |
| AGI limit (credit reaches $0) | $19,104 |
| Investment income limit | $11,600 |

### Calculation

The EIC is calculated using IRS tables (not a simple formula). For estimation:

```
if earned_income <= 8,490:
    # Phase-in: credit increases as income rises
    credit = earned_income * 0.0765
elif earned_income <= 10,330:
    # Plateau: maximum credit
    credit = 649
else:
    # Phase-out: credit decreases as income rises
    credit = max(649 - (earned_income - 10,330) * 0.0765, 0)

# Also check AGI separately -- use the LOWER credit
# if earned income and AGI differ (unlikely for W-2 only)
agi_credit = max(649 - (AGI - 10,330) * 0.0765, 0) if AGI > 10,330 else credit_from_above

final_credit = min(credit, agi_credit)
```

### Where It Goes on Form 1040
- Calculated using EIC Worksheet or Schedule EIC
- Goes to Form 1040, Line 27
- This is a REFUNDABLE credit -- it goes on the payments side, not the credits side

### EZFile Note
Most W-2 filers earning above $19,104 will not qualify. But someone who worked part of the year, was a student who worked part-time, or has a very low-wage job may qualify. The age requirement (25-64) is strict.

## 3. Credits NOT Available to This Profile

These credits exist but are NOT available to single filers with no dependents and W-2-only income:

| Credit | Why Not Available |
|---|---|
| Child Tax Credit ($2,200 for 2025) | No children |
| Child and Dependent Care Credit | No dependents |
| American Opportunity Credit | Requires 1098-T (education), out of scope v1 |
| Lifetime Learning Credit | Requires 1098-T, out of scope v1 |
| Adoption Credit | No adoption |
| Premium Tax Credit | Requires Form 1095-A (marketplace insurance), out of scope v1 |
| Foreign Tax Credit | No foreign income |
| Residential Energy Credit | No home ownership |

## Credit Application Order

Credits are applied in a specific order on Form 1040:

1. **Nonrefundable credits** (reduce tax to $0 but not below):
   - Line 19: Saver's Credit + other nonrefundable credits
   - Line 22 = Line 16 (tax) - Line 19 (credits) -- cannot go below $0

2. **Other taxes** (add to Line 22):
   - Line 23: Additional taxes (usually $0 for this profile)
   - Line 24 = Line 22 + Line 23 = Total Tax

3. **Refundable credits** (added to payments side):
   - Line 27: Earned Income Credit
   - These are added to withholding (Line 25a) to get total payments (Line 33)

4. **Final calculation:**
   - If Line 33 (payments) > Line 24 (total tax): REFUND = Line 33 - Line 24
   - If Line 24 > Line 33: AMOUNT OWED = Line 24 - Line 33
