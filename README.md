# EZFile - W-2 Tax Filing Assistant

A Claude Code plugin that helps single W-2 filers calculate their federal tax return and file for free at [Free File Fillable Forms](https://www.freefilefillableforms.com/).

Named after the discontinued IRS Form 1040-EZ, which served exactly this demographic before the IRS retired it in 2018.

## Who This Is For

- Single filer (not married)
- No children or dependents
- W-2 wage income only (no freelance, 1099s, investments)
- Renter (no mortgage or property tax)
- May have federal student loans (1098-E)
- Tax Year 2025

If your situation is more complex, EZFile will tell you and recommend a CPA or full-service tax software.

## Installation

```bash
# Clone the plugin
git clone https://github.com/ezfile/ezfile.git ~/ezfile

# Use with Claude Code
claude --plugin-dir ~/ezfile
```

Or add to your Claude Code settings to load automatically.

## Try It Out

A sample W-2 is included in the repo so you can test EZFile without using real tax documents:

```
/ezfile:file-taxes ~/ezfile/Sample-W2.pdf
```

The sample contains fictional data — no real personal information.

## Usage

### Main Workflow

```
/ezfile:file-taxes ~/Documents/my-w2.pdf
```

This single command:
1. Reads your W-2 (PDF or image)
2. Extracts and validates all box values
3. Masks your SSN (only last 4 digits shown)
4. Asks a few intake questions (date of birth, student loans, tips, overtime)
5. Calculates your complete Form 1040 line by line
6. Shows your refund or amount owed
7. Provides a filing guide for freefilefillableforms.com

### Additional Commands

| Command | Description |
|---|---|
| `/ezfile:add-1098e <amount\|path>` | Add student loan interest deduction |
| `/ezfile:calculate` | Recalculate your return after changes |
| `/ezfile:review` | Display your return summary |
| `/ezfile:explain <topic>` | Explain any tax concept in plain English |
| `/ezfile:checklist` | Step-by-step guide to file at freefilefillableforms.com |

### Example

```
> /ezfile:file-taxes ~/Documents/w2-2025.pdf

  Reading W-2...

  Employer:  Acme Corp
  Wages (Box 1):           $52,000.00
  Federal tax withheld:     $8,400.00
  SSN: XXX-XX-4567

  A few questions:
  - Date of birth? → 1995-03-15
  - Student loan interest? → $1,200
  - Tips at work? → No
  - Overtime pay? → No
  - New car purchase in 2025? → No

  Calculating...

  FEDERAL RETURN SUMMARY
  Wages:                    $52,000.00
  Student loan interest:    -$1,200.00
  AGI:                      $50,800.00
  Standard deduction:      -$15,750.00
  Taxable income:           $35,050.00

  Tax:
    10% on $11,925:          $1,192.50
    12% on $23,125:          $2,775.00
  Total tax:                 $3,967.50

  Federal withheld:          $8,400.00
  YOUR REFUND:               $4,432.50
```

## What's New for 2025

- **Schedule 1-A deductions**: New above-the-line deductions for tips, overtime, car loan interest, and seniors
- **Updated standard deduction**: $15,750 (Single under 65), $17,750 (Single 65+)
- **Updated student loan phaseouts**: $85,000-$100,000 (Single)
- **Form 1040-SR**: Automatically offered for filers born before January 2, 1961

## Privacy & Security

EZFile is designed with privacy as a core principle:

- **Local only**: All processing happens on your machine. Tax data never leaves your computer.
- **SSN masking**: Full SSNs are never stored or displayed. Only the last 4 digits are shown.
- **Network blocking**: Hooks prevent any network commands (curl, wget, etc.) from running.
- **PII protection**: Hooks block SSN/EIN patterns from appearing in web searches.
- **Output scanning**: Written files are scanned for accidentally exposed SSNs.

## Supported Tax Situations

| Feature | Supported |
|---|---|
| W-2 wage income | Yes |
| Standard deduction | Yes |
| Student loan interest (1098-E) | Yes |
| Schedule 1-A (tips, overtime, car loan, senior) | Yes |
| Form 1040 | Yes |
| Form 1040-SR (seniors) | Yes |
| Saver's Credit | Yes |
| EIC (no children) | Yes |
| State returns (PA, NY, CA, no-income-tax states) | Yes |

## Not Supported (Use a CPA or TurboTax)

- Married or has dependents/children
- Homeowner (mortgage interest, property tax)
- Self-employed or 1099 income
- Investment income (stocks, crypto, dividends)
- Itemized deductions
- Multiple states

## Disclaimer

> **EZFile is a tax calculation assistant, not a licensed tax preparer or tax advisor. It does not file your taxes -- you must file yourself at freefilefillableforms.com or another IRS-approved method. Review all numbers carefully before entering them. You are responsible for the accuracy of your tax return. For complex situations, consult a CPA or enrolled agent.**

## License

MIT
