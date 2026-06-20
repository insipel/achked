#!/usr/bin/env python

class Clock:

    def __init__(self, hour, mins):
        self.hour = 0;
        self.mins = 0;

        if (hour < 13):
            self.hour = hour;
        if (mins < 60):
            self.mins = mins;

    def __str__(self):
        return "%dHr:%dMins" % self.hour, self.mins


def main():
    pass

if __name__ == '__main__':
    main()

