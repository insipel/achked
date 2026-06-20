#!/usr/bin/env python

class Thing:
    number = 0

    def __init__(self):
        Thing.number += 1
        self.thing_number = self.number

print Thing().thing_number
