#!/usr/bin/env python3
"""
password_generator.py
Generate strong passwords using cryptographically secure randomness.
Usage examples:
  python password_generator.py
  python password_generator.py -l 20 -n 3 --no-ambiguous
"""
import argparse
import secrets
import string

AMBIGUOUS = set("O0oIl1|`'\"~ ")

def secure_shuffle(seq):
    # Fisher–Yates using secrets.randbelow for cryptographic shuffling
    for i in range(len(seq) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        seq[i], seq[j] = seq[j], seq[i]

def generate_password(length=16, lower=True, upper=True, digits=True,
                      symbols=True, no_ambiguous=False):
    pools = []
    if lower:   pools.append(string.ascii_lowercase)
    if upper:   pools.append(string.ascii_uppercase)
    if digits:  pools.append(string.digits)
    if symbols: pools.append("!@#$%^&*()-_=+[]{};:,.?/")

    if not pools:
        raise ValueError("Select at least one character type.")

    if no_ambiguous:
        pools = [''.join(ch for ch in s if ch not in AMBIGUOUS) for s in pools]

    if length < len(pools):
        raise ValueError(f"Length must be ≥ {len(pools)} to include each type.")

    # Ensure at least one char from each selected pool
    password_chars = [secrets.choice(pool) for pool in pools]
    all_chars = ''.join(pools)

    # Fill the rest
    for _ in range(length - len(password_chars)):
        password_chars.append(secrets.choice(all_chars))

    secure_shuffle(password_chars)
    return ''.join(password_chars)

def main():
    p = argparse.ArgumentParser(description="Generate strong passwords.")
    p.add_argument("-l", "--length", type=int, default=16,
                   help="Password length (8–128). Default: 16")
    p.add_argument("-n", "--count", type=int, default=1,
                   help="How many passwords to generate. Default: 1")
    # Toggle flags (all enabled by default)
    p.add_argument("--no-lower",  dest="lower",  action="store_false",
                   help="Exclude lowercase letters")
    p.add_argument("--no-upper",  dest="upper",  action="store_false",
                   help="Exclude uppercase letters")
    p.add_argument("--no-digits", dest="digits", action="store_false",
                   help="Exclude digits")
    p.add_argument("--no-symbols", dest="symbols", action="store_false",
                   help="Exclude symbols")
    p.add_argument("--no-ambiguous", action="store_true",
                   help="Exclude ambiguous characters like O,0,l,1,|")
    p.set_defaults(lower=True, upper=True, digits=True, symbols=True)

    args = p.parse_args()
    if not (8 <= args.length <= 128):
        p.error("Length must be between 8 and 128.")

    for _ in range(args.count):
        print(generate_password(args.length, args.lower, args.upper,
                                args.digits, args.symbols, args.no_ambiguous))

if __name__ == "__main__":
    main()
