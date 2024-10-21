#!/usr/bin/python3
'''this is module takes an mark down written file
and produce new html file based on it'''

import sys


def parseLine(line):
    '''function that do the parsing
    args:
        line (str): a string ended with newline character to be parsed
    '''
    count = 0
    if line[0] == '#':
        for ch in line:
            if ch == '#':
                count += 1
            else:
                break
        preTag = f"<h{count}>"
        postTag = f"</h{count}>"
        bodyStr = ""
        for ch in line:
            if ch == "#":
                continue
            if ch == "\n":
                return preTag + bodyStr + postTag + ch
            bodyStr += ch
    else:
        return line
    return preTag + bodyStr + postTag


def parseList(lines):
    ulCount = 0
    olCount = 0
    newlines = []
    newlines2 = []
    for line in lines:
        if line[0] == '-':
            if ulCount == 0:
                newlines.append("<ul>\n")
            ulCount += 1
        elif ulCount != 0:
            newlines.append("</ul>\n")
            ulCount = 0
        newlines.append(line)

    for line in newlines:
        if line[0] == '*' and line[1] == ' ':
            if olCount == 0:
                newlines2.append("<ol>\n")
            olCount += 1
        elif olCount != 0:
            newlines2.append("</ol>\n")
            olCount = 0
        newlines2.append(line)
    return newlines2


def parseListItems(lines):
    newLines = []
    for line in lines:
        mystr = ""
        pre = "<li>"
        post = "</li>"
        for index, ch in enumerate(line):
            if ch == "-" or ch == "*" and line[index + 1] == " ":
                mystr = pre + mystr
                continue
            if ch == "\n" and pre in mystr:
                mystr = mystr + post
            mystr += ch
        newLines.append(mystr)
    return newLines


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)
    try:
        with open(sys.argv[1], "r") as srcFile:
            content = srcFile.readlines()
            with open(sys.argv[2], "w") as desFile:
                contentAfterHeader = []
                for line in content:
                    contentAfterHeader.append(parseLine(line))
                contentAfterHeader = parseList(contentAfterHeader)
                contentAfterHeader = parseListItems(contentAfterHeader)
                for item in contentAfterHeader:
                    desFile.write(item)
    except FileNotFoundError as e:
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        exit(1)
