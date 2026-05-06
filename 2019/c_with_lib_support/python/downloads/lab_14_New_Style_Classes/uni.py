#!/usr/bin/env python
# coding: utf-8   
# necessary for python not to complain
# about "¥" in the string at the bottom.

# If this doesn't work for your Mac, try:
# export PYTHONIOENCODING=utf-8 
# in your ~/.profile or ~/.bashrc
# or at your shell prompt.

'''Unicode handling for 2.6.
'''
class Currency(float):
    def __str__(self):
        return  self.symbol +  float.__str__(self)

class Yen(Currency):
    symbol = unichr(165)

def main():
    y = Yen(100)
    print unicode(y)

main()

"""
¥100.0
"""
