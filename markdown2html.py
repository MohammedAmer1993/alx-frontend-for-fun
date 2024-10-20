#!/usr/bin/python3
'''this is module takes an mark down written file
and produce new html file based on it'''

import sys


def parser(line):
    '''function that do the parsing
    args:
        line (str): a string ended with newline character to be parsed
    '''
    pass


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)
    try:
        with open(sys.argv[1], "r") as srcFile:
            content = srcFile.readlines()
            with open(sys.argv[2], "w") as desFile:
                for line in content:
                    desFile.write("parser(line)")
    except FileNotFoundError as e:
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        exit(1)
