#!/usr/bin/env python3
import sys


def calculate_simple_interest(principal, rate, time):
    interest = principal * (rate / 100) * time
    amount = principal + interest
    return amount, interest


def main():
    if len(sys.argv) != 4:
        print("Usage: python3 tools/simple_interest.py <principal> <annual_rate> <years>")
        sys.exit(1)

    try:
        principal = float(sys.argv[1])
        rate = float(sys.argv[2])
        time = float(sys.argv[3])
    except ValueError:
        print("All arguments must be numeric.")
        sys.exit(1)

    if time < 0:
        print("Time must be non-negative.")
        sys.exit(1)

    amount, interest = calculate_simple_interest(principal, rate, time)

    print(f"Final amount: ${amount:,.2f}")
    print(f"Interest earned: ${interest:,.2f}")


if __name__ == "__main__":
    main()
