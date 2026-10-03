#!/usr/bin/env python3
import sys


def calculate_compound_interest(principal, annual_rate, compounds_per_year, years):
    amount = principal * (1 + annual_rate / 100 / compounds_per_year) ** (compounds_per_year * years)
    interest = amount - principal
    return amount, interest


def main():
    if len(sys.argv) != 5:
        print("Usage: python3 tools/compound_interest.py <principal> <annual_rate> <compounds_per_year> <years>")
        sys.exit(1)

    try:
        principal = float(sys.argv[1])
        annual_rate = float(sys.argv[2])
        compounds_per_year = float(sys.argv[3])
        years = float(sys.argv[4])
    except ValueError:
        print("All arguments must be numeric.")
        sys.exit(1)

    if compounds_per_year <= 0 or years < 0:
        print("Compounds per year must be positive and years must be non-negative.")
        sys.exit(1)

    amount, interest = calculate_compound_interest(principal, annual_rate, compounds_per_year, years)

    print(f"Final amount: ${amount:,.2f}")
    print(f"Interest earned: ${interest:,.2f}")


if __name__ == "__main__":
    main()
