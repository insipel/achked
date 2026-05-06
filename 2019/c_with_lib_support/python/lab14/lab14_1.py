#!/usr/bin/env python

class SortedDictionary(dict):

    """ Not needed: def __init__(self): """

    def keys(self):
        """ return [x for x in sorted(self)] """
        print "keys func"
        return sorted(self)

    def GetKeys(self):
        my_keys = [x for x in dict.keys(self)]
        my_keys.sort()
        print my_keys
        return my_keys

    def __iter__(self):
        print "temp"
        for x in self.GetKeys():
            print x
            yield x

def main():
    sDict = SortedDictionary()

    sDict.update({11:'70',32:'60',53:'50'})
    print ','.join([str(x) for x in sDict])
    """ print sDict.keys() """
    print sDict.keys()

if __name__ == '__main__':
    main()

