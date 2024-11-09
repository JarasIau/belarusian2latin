#!/usr/bin/env python3
# A CLI wrapper for the original script
import argparse
import belarusian2latin

def get_args():
    parser = argparse.ArgumentParser(description="belarusian2latin - convert belarusan text in cyrillic to latin", epilog="All rights to the original script belong to sevelev-ens")
    parser.add_argument("-t", "--text", type=str, help="convert given text and write to standard output")
    parser.add_argument("-f", "--file", type=str, help="convert file's content and write to standard output")
    return parser.parse_args()

def main():
    args = get_args()
    if args.file:
        with open(args.file) as f:
            print(belarusian2latin.latinize(f.read()))
    else:
        print(belarusian2latin.latinize(args.text))

if __name__ == "__main__":
    main()
