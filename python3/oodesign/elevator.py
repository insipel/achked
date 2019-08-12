#!/usr/bin/env python3

from enum import Enum
from threading import Thread
from heapq import *
import re

class Direction(Enum):
    UP = 1
    DOWN = 1

class Door_Status(Enum):
    OPEN = 1
    CLOSED = 1

class EV_State(Enum):
    MOVING = 1
    STOPPED = 2

class Request():
    def __init__(self, req_time, in_floor, direction):
        self.in_floor = in_floor
        self.time = req_time
        self.dir = direction

    def __lt__(self, o):
        if self.in_floor > o.in_floor:
            return True
        else:
            return False

class Elevator():

    def __init__(self):
        self.dir = Direction.UP
        self.door = Door_Status.CLOSED
        self.cur_floor = 0
        self.ev_state = EV_State.STOPPED

        # Listener to requests and the proecssor of those requests
        self.listener = None;
        self.processor = None;

        self.upQ   = []
        self.downQ = []
        self.currentQ = self.upQ

        print("created elevator object")

    def start_listener(self):
        fd = open("test.txt")
        for line in fd:
            line = line.rstrip("\n")
            line = line.split(" ")
            # Get either 'call' request to EV or 'go' request to the
            # EV.
            if line[0] == "Call":
                # Call request is from a floor and with a direction
                # going up or down
                self.call(int(line[1]), Direction.UP if line[2] ==
                        "up" else Direction.DOWN)
            else:
                # Go request is only to the dest floor
                self.go(int(line[1]))

    def go(in_floor):
        self.call(in_floor, self.dir)

    def call(in_floor, direction):
        new_req = Request(time.time(), in_floor, direction)

        # Lock for queue modification
        self.process_q_condvar.acquire()
        if direction == Direction.UP:
            if in_floor >= self.cur_floor:
                heappush(self.currentQ, new_req)
            else:
                heappush(self.upQ, new_req)

        else:
            if in_floor <= self.cur_floor:
                heappush(self.currentQ.append(new_req)
            else:
                heappush(self.downQ.append(new_req)

        # Release the lock after queue modification
        self.process_q_condvar.signal() # As the elevator might be
                                        # waiting for this signal.
        self.process_q_condvar.release()

    def start_processor(self):
        self.process()

    def process(self):
        while True:
            # If either upQ or downQueue is valid, then we can
            # continue to process
            #if not self.upQ and not self.downQ:
            if not self.upQ or not self.downQ:
                if currentQ:

                    self.process_q_condvar.acquire()
                    req = heappop(currentQ)
                    self.process_q_condvar.release()

                    process_goto_floor(req.floor)
                else:
                    # Current queueu is empty, so process the next one.
                    process_next_queue()
            else:
                # Take a break before checking for the next request.
                # Most likely it'd be a condvar.wait()
                self.process_q_condvar.wait()

    def process_next_queue(self):

        self.process_q_condvar.acquire()
        if self.direction = Direction.UP:
            self.direction = Direction.DOWN
            self.currentQ = self.downQ
            self.downQ = []
        else:
            self.direction = Direction.UP
            self.currentQ = self.upQ
            self.upQ = []
        self.process_q_condvar.release()

    def process_goto_floor(dest_floor):
        self.state = State.MOVING
        for i in range(self.cur_floor, dest_floor):
            # simulate going to the floor and opening the door and
            # spening a tiny bit of time there.
            time.sleep(2)

        self.location = dest_floor
        self.door = Door_Status.OPEN
        self.state = State.STOPPED

        # wait for time to open the door, let the people come into the
        # EV and then close the door
        time.sleep(5) # 5 seconds

        self.door = Door_Status.CLOSED

def main():
    ev = Elevator()
    ev.start_listener()
    ev.start_processor()

    print("Dir: ", ev.dir, ", door: ", ev.door)

if __name__ == "__main__":
    main()

