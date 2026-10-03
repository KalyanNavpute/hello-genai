principal = 15847
annual_rate = 0.0734
months = 8 * 12 + 7
compound_periods = 12

amount = principal * (1 + annual_rate / compound_periods) ** months
interest = amount - principal

print(f"Principal: ${principal:,.2f}")
print(f"Annual rate: {annual_rate * 100:.2f}%")
print(f"Compounding periods: {compound_periods} per year")
print(f"Total months: {months}")
print(f"Final amount: ${amount:,.2f}")
print(f"Total interest: ${interest:,.2f}")
