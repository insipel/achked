#!/usr/bin/env python
""" Lab 06 excercise 3"""

def MakeString(input_list, glue_str = ', '):
    return(glue_str.join(str(x) for x in input_list))

def main():
    print "|%s|" % MakeString([])
    print "|%s|" % MakeString("")
    print "|%s|" % MakeString(())

    print "|%s|" % MakeString(((0), 2, 4), "# ")
    print "|%s|" % MakeString((1, ))

if __name__ ==  '__main__':
    main()

