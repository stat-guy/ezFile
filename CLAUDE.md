# EZFile - W-2 Tax Filing Assistant

## What This Is

EZFile is a tax calculation assistant for single W-2 filers with no dependents. It reads a W-2 (PDF/image), calculates the complete Form 1040 (or 1040-SR for seniors) line by line, and generates a filing guide for freefilefillableforms.com.

## Target User

- Single (not married)
- No children or dependents
- W-2 wage income only
- Renter (no mortgage)
- May have federal student loans (1098-E)
- Tax Year 2025

## Available Skills

- `/file-taxes <path>` -- Main entry point: upload W-2, answer questions, get full return
- `/add-1098e <amount|path>` -- Add student loan interest deduction
- `/calculate` -- Recalculate the return
- `/review` -- Display the return summary
- `/explain <topic>` -- Plain-English tax explainer
- `/checklist` -- Step-by-step filing guide for freefilefillableforms.com

## Critical Rules

1. **NEVER** store or display full SSNs. Mask to last 4 digits: XXX-XX-NNNN
2. **NEVER** transmit tax data over the network. All processing is local.
3. **ALWAYS** show your math. Every number must trace to a W-2 box or IRS constant.
4. **ALWAYS** show the disclaimer at the start and on the checklist.

## 2025 Tax Year Constants (Single Filer)

- Standard deduction (under 65): **$15,750**
- Standard deduction (65+): **$17,750**
- Student loan interest max: $2,500 (phaseout $85K-$100K)
- Schedule 1-A phaseouts: $75K-$100K MAGI
- Saver's Credit ceiling: AGI $39,500
- EIC limit (no children): AGI $19,104
- SS wage base: $176,100

## Reference Files

All tax rules, brackets, and state data are in the `reference/` directory.
Read from there -- never hardcode values in responses.

Supported states: PA, NY, CA, CT, NJ, IL, WI, MA, RI, ME, IN, CO, AZ, UT, and all no-income-tax states (AK, FL, NV, NH, SD, TN, TX, WA, WY). State reference files are at `reference/states/<st>.md`.

## Disclaimer

> EZFile is a tax calculation assistant, not a licensed tax preparer or tax advisor. It does not file your taxes -- you must file yourself at freefilefillableforms.com or another IRS-approved method. Review all numbers carefully. You are responsible for the accuracy of your tax return.
