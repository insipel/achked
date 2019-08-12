#!/usr/bin/env python3

# threading is a module, collection of functions and attributes
# Lock, Condition are atrributes in the threading module
import threading
#
# Thread is class that'll be used by Producer and Server classes to
# inherit from.
from threading import Thread

import random
import sys # For argv, argc
import time


#Create 'Server' threads and their respective queues and hashmap.
keys = ['key01', 'key02', 'key03', 'key04', 'key05', 'key06', 'key07',
        'key08', 'key09', 'key10', 'key11', 'key12', 'key13', 'key14']
#keys = ['key01', 'key02', 'key03', 'key04']
all_msg_q = [] # Made global only for debugging purpose.
all_smap = [] # Made global only for debugging purpose.

NUM_Qs = 5
NUM_PROD_THDS = 2
MAX_Q_SZ = 40
PROD_SLEEP = 1
SERV_SLEEP = 2

# Used for controlling total number of messages from testing point of
# view
total_msg_lock = threading.Lock()
pmap = {}
MAX_MSGS = 100
total_msgs = 0
server_done = False

class MsgQ():
    def __init__(self, qid):
        self.qid = qid
        self.sq = []
        self.mutex = threading.Lock()
        self.available = threading.Condition(self.mutex)
        self.empty = threading.Condition(self.mutex)
        print("created message queue id: ", self.qid)

class Server(Thread):
    def __init__(self, serv_id, msg_q, smap):
        Thread.__init__(self)
        self.msg_q = msg_q
        self.smap = smap
        self.daemon = True
        self.serv_id = serv_id
        self.start()

    def run(self):
        global total_msgs, server_done
        msgid = 0

        while True:

            self.msg_q.available.acquire()

            while not server_done and len(self.msg_q.sq) == 0:
                #print("nothing in the queue, going to wait")
                self.msg_q.available.wait()
                #print("got something in the queue, check it out")

            if server_done:
                break

            key, count, msgid = self.msg_q.sq.pop(0)
            if key not in self.smap:
                self.smap[key]  = 0
            self.smap[key] += count
            self.msg_q.empty.notify()
            self.msg_q.available.release()

            time.sleep(random.random() * SERV_SLEEP)

            print("Server#: ", self.serv_id, " Msg#: ", msgid,
                    " key: ", key, " count: ", count,
                    " total: ", self.smap[key])
            if msgid >= MAX_MSGS:
                server_done = True
                self.notify_other_servers()
                break

        print("Server thread# ", self.serv_id, " done!")

    def notify_other_servers(self):
        global all_msg_q

        for i in range(NUM_Qs):
            all_msg_q[i].available.acquire()
            all_msg_q[i].available.notify()
            all_msg_q[i].available.release()
        

class Producer(Thread):
    def __init__(self, pid, all_msg_q):
        # all_msg_q is a list of all the MsgQ instances
        Thread.__init__(self)
        self.all_msg_q = all_msg_q
        self.pid = pid
        self.start()

    def run(self):
        global total_msgs

        while True:
            count = int((random.random()+1) * 10)

            key_idx = int(random.random() * len(keys))
            key_hash = hash(keys[key_idx])
            qidx = key_hash % NUM_Qs
            #print(key_hash, qidx)

            # Test part of the code to control the test execution
            total_msg_lock.acquire()
            if total_msgs >= MAX_MSGS:
                total_msg_lock.release()
                break
            total_msgs += 1
            total = total_msgs
            key = keys[key_idx]
            if key not in pmap:
                pmap[key] = 0
            pmap[key] += count
            total_msg_lock.release()

            #key_hash = hashlib.sha1(keys[key_idx].encode())
            #hex_dig = key_hash.hexdigest()
            #print(type(hex_dig))
            #qidx = int(hex_dig) % NUM_Qs

            self.all_msg_q[qidx].available.acquire()
            #print("Prod ", self.pid, " acquired lock: qidx:", qidx)

            while len(self.all_msg_q[qidx].sq) > MAX_Q_SZ:
                #print("Waiting on msg q to become empty")
                self.all_msg_q[qidx].empty.wait()
                #print("Msg q has space now!")

            self.all_msg_q[qidx].sq.append((keys[key_idx], count, total))
            self.all_msg_q[qidx].available.notify()
            self.all_msg_q[qidx].available.release()

            print("Producer:", self.pid, " msg#: ", total, " key:", keys[key_idx], " count: ", count, " qid:", qidx) 

            time.sleep(int(random.random() * PROD_SLEEP))

def main(argv):
    #print("Number of args:", len(argv))
    #print("Arguments are:", argv)
    global all_msg_q
    global all_smap

    for i in range(NUM_Qs):
        all_msg_q.append(MsgQ(i))
        all_smap.append({})

    prod_thds = []
    serv_thds = []

    # 10 threads
    for i in range(NUM_PROD_THDS):
        prod_thds.append(Producer(i, all_msg_q))

    for i in range(NUM_Qs):
        serv_thds.append(Server(i, all_msg_q[i], all_smap[i]))

    if argv[1] == "producer":
        print("start producers")
    elif argv[1] == "consumer":
        print("start consumers")

    for i in range(NUM_PROD_THDS):
        prod_thds[i].join()

    for i in range(NUM_Qs):
        serv_thds[i].join()

    print("Producer generated:")
    print(pmap)

    print("Cosumers counted:")
    all_match = True
    for smap in all_smap:
        for key in smap:
            if smap[key] != pmap[key]:
                print("Mismatch for key: ", key, " prod count: ",
                        pmap[key], " server count: ", smap[key])
                all_match = False

    if all_match:
        print("server counted correctly")

    print("Bye!")

if __name__ == "__main__":
    main(sys.argv)

