import sys

from .core import lookup

HELP = """
MicroWhois v0.1

Usage

python3 -m microwhois <domain>

Example

python3 -m microwhois example.com
"""

def main():

    args = sys.argv[1:]

    if not args:
        print(HELP)
        return

    lookup(args[0])
