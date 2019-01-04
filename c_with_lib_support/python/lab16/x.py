#!/usr/bin/env python

def Snake(rattle=()):
    rattle += ("hiss",)
    print rattle
    print id(rattle)

Snake()
Snake()
Snake()
a = ()

print "---------"
print hex(id(a))
a += ("hiss",)
print hex(id(a))
a += ("hiss",)
print hex(id(a))
a += ("hiss",)
print hex(id(a))

