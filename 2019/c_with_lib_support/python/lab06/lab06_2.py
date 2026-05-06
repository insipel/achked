#!/usr/bin/env python

# Part B
print "Part B: ",
print str(" + ".join([str(x) for x in range(10)]))

# Part C
print "Part C (method 1) : ",
alist = ["Bo", "Li", "On", "An"]
alist = [(x, "Wu") for x in sorted(alist)]
alist = ", ".join(["%s %s" % (first, last) for (first, last) in alist])
print alist

print "Part C (method 2) : ",
blist = ", ".join(["%s Wu" % first for first in sorted(["Bo", "Li", "On", "An"])])
print blist

#Part D
print "Part D: "
alist = "\n".join(["%2s.1" % str(y) for y in [x for x in range(0,40,10)]])
print alist

