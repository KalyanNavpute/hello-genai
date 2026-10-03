# Use Simple Interest Agent Instructions

Use this agent when the user asks to calculate simple interest, especially when they provide:
- a principal amount
- an annual interest rate
- a time period in years

## Tool to use
Use the Python script at `tools/simple_interest.py`.

## When to invoke the tool
Invoke the tool when the user wants a quick calculation of:
- the final amount after simple interest is applied
- the interest earned or paid over a period of time

Use this tool for simple-interest calculations only. Do not use it for compound-interest or amortized loan calculations.

## Command-line usage
Run the script as:

```bash
python3 tools/simple_interest.py <principal> <annual_rate> <years>
```

### Example
```bash
python3 tools/simple_interest.py 1000 5 3
```

### Arguments
- `<principal>`: starting amount of money
- `<annual_rate>`: annual interest rate as a percentage, for example `5`
- `<years>`: total time period in years

## How to present results
After running the tool, present the results in a clear, concise format:

- Final amount: `$X.XX`
- Interest earned: `$X.XX`

Use two decimal places for currency values.

If the user asks for the formula, briefly explain that the script uses:

```text
I = P × r × t
A = P + I
```

where:
- `I` is the interest
- `P` is the principal
- `r` is the annual rate expressed as a decimal or percentage used consistently in the formula
- `t` is the time in years
- `A` is the final amount

Keep the response concise and user-friendly while still showing the actual computed result.
