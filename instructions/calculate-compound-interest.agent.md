# Calculate Compound Interest Agent Instructions

Use this agent when the user asks to calculate compound interest for an investment or loan, especially when they provide:
- a principal amount
- an annual interest rate
- a compounding frequency (for example, monthly, quarterly, daily)
- a total time period in years

## Tool to use
Use the Python script at `tools/compound_interest.py`.

## When to invoke the tool
Invoke the tool when the user wants the result of a compound-interest calculation, including:
- final amount after interest is applied
- total interest earned or paid
- a quick numerical calculation from supplied values

Do not use this tool for simple interest problems or for calculations that require a different financial formula.

## Command-line usage
Run the script as:

```bash
python3 tools/compound_interest.py <principal> <annual_rate> <compounds_per_year> <years>
```

### Example
```bash
python3 tools/compound_interest.py 15847 7.34 12 8.583333333333334
```

### Arguments
- `<principal>`: starting amount of money
- `<annual_rate>`: annual interest rate as a percentage, for example `7.34`
- `<compounds_per_year>`: how many times interest is compounded each year, for example `12` for monthly
- `<years>`: total time period in years

## How to present results
After running the tool, present the results in a clear, concise format:

- Final amount: `$X.XX`
- Interest earned: `$X.XX`

Include the values as money with two decimal places.

If the user asks for the formula or reasoning, briefly explain that the script uses:

```text
A = P(1 + r/n)^(nt)
```

where:
- `A` is the final amount
- `P` is the principal
- `r` is the annual rate expressed as a decimal
- `n` is the number of compounding periods per year
- `t` is the total time in years

Keep the response concise and user-friendly while still showing the actual computed result.
