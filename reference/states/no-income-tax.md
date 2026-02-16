# States With No Income Tax

The following states do not levy a state income tax on wages:

| State | Abbreviation | Notes |
|---|---|---|
| Alaska | AK | No state income tax; no state sales tax either |
| Florida | FL | No state income tax |
| Nevada | NV | No state income tax |
| New Hampshire | NH | No tax on W-2 wages; previously taxed interest/dividends (repealed 2025) |
| South Dakota | SD | No state income tax |
| Tennessee | TN | No tax on W-2 wages; previously taxed interest/dividends (repealed 2021) |
| Texas | TX | No state income tax |
| Washington | WA | No state income tax on wages; has a capital gains tax (not applicable to W-2 filers) |
| Wyoming | WY | No state income tax |

## EZFile Handling

If the W-2 Box 15 shows one of these states (or Box 15 is blank / shows no state):

1. **No state return is needed** for income tax purposes
2. Tell the user: "Great news -- [State] has no state income tax, so you only need to file a federal return."
3. Skip all state tax calculations
4. If Box 17 (state tax withheld) shows $0 or is blank, this confirms no state return needed
5. If Box 17 shows a non-zero amount for a no-income-tax state, flag this as unusual and suggest the user verify with their employer

## Local Taxes

Some of these states may still have local taxes:
- **Alaska:** Some municipalities levy a local income tax or sales tax
- **Washington:** Has a capital gains tax and some local B&O taxes (not W-2 related)

For W-2 filers, check Box 18/19/20 for any local tax withholding even in no-income-tax states.

## What to Tell the User

> "You live in [State], which doesn't have a state income tax. That means you only need to file your federal return -- no state paperwork needed. This saves you time and means your entire refund comes from the federal government."
