#! /usr/bin/env python3

""" sortclipboard.py
Alphanumerically sorts a string delimited either
by '\n', ',' or ' '. 

Usage:
    - First way:  sortclipboard.py #C #D #A #B #E #G #H #I #J
        Writes to standard output: #A #B #C #D #E #G #H #I #J
    - Second way: sortclipboard.py
        Takes the text in the clipboard (if any), sorts it,
        copies it back to the clipboard, and writes it to
        standard output.
"""

import sys
import pyperclip
from titlecase import titlecase
import re

# -------------------------------------------------------------------
def main():
    """ Main function. """
    clipboard = False
    argv = sys.argv[1:]

    if not argv or argv[0] == '':
        # try clipboard
        inputtext = pyperclip.paste()
        if inputtext != "".strip():
            clipboard = True
        else:
            # no arguments, no clipboard text
            sys.exit(1)
    else:
        inputtext = ' '.join(argv)
        inputtext = inputtext.strip()

    # print(f"inputtext: {inputtext}")

    delim = ""

    # search for delim
    if re.search(r"\n", inputtext):
        delim = r"\n"
    elif re.search(r",", inputtext):
        delim = ","
    elif re.search(r" ", inputtext):
        delim = " "
    else:
        print("Error: No separator ('\\n', ',', '  ') found")
        sys.exit(1)

    # https://www.geeksforgeeks.org/python-sort-words-separated-by-delimiter/
    outputtext = delim.join(sorted(inputtext.split(delim)))

    if clipboard:
        pyperclip.copy(outputtext)

    print(outputtext, file=sys.stdout)


# ------------------------------------------------------------
if __name__ == '__main__':
    main()
