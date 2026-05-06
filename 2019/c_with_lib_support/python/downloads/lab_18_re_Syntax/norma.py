#!/usr/bin/env python
"""Using re to print the city and state where Norma lives.
"""
import re  
def GetTownState(text, first_name):
    m = re.search(r"""
    ^%s      # Line starts with the name
    \b       # followed by a non-word character
    (?:      # Un-captured group with anything
    [^:]+    # except colons,  followed by a
    :){2}    # colon. That group twice.
    [^,]+    # All characters up to a comma,
    ,[ ]+    # a comma and some spaces. 
    (?P<town># Capturing a group and naming it "town". 
    [^\d]+)  # with anything but digits
    \d       # a digit ends the match
    """ % first_name, text, re.VERBOSE | re.MULTILINE)
    if m:
        return m.group("town")
    return "Not Found"

def ReadFile(file_name):
    try:
        fp = open(file_name)
        try:
            text = fp.read()
        finally:
            fp.close()
    except IOError:
        print "Can't open %s" % file_name
        return None
    return text
def main():
    print GetTownState(ReadFile('address.data'), "Norma")
if __name__ == '__main__':
    main()
"""
$ norma.py
 Dearborn, MI        """
