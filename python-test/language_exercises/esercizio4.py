# ex 4

import sys

def read(arg):
    html = ""
    c = 0
    for value in arg:
        if (c != 0):
            html += '<p>' + value + '</p>\n'
        c = c+1
    return html

print read(sys.argv)