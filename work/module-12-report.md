# Module 12 Completion Report

## Instruction File
- Filename: .agent.md

# Greeting Tool Agent

Use the Python script `greeting_tool.py` to print a friendly greeting.

## Behavior
- Accepts a required `--name` argument
- Prints: `Hello, {name}!`
- Supports `--help` to show usage

## Example
```bash
python greeting_tool.py --name "World"
```

## Script File
- Filename: greeting_tool.py
- Language: Python

#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(description="Print a friendly greeting.")
    parser.add_argument("--name", default="World", help="Name to greet.")
    args = parser.parse_args()
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()

## Script Execution Output
usage: greeting_tool.py [-h] [--name NAME]

Print a friendly greeting.

optional arguments:
  -h, --help   show this help message and exit
  --name NAME  Name to greet.
Kalyan_Navpute@EPINPUNW01FC hello-genai %
