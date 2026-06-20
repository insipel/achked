#!/usr/bin/env python3

from heapq import *

class Bld_point:
    def __init__(self, x, is_st, ht):
        self.x = x
        self.is_st = is_st
        self.ht = ht

    def __lt__(self, o):
        #print("lt: self:(", self.x, self.is_st, self.ht,"), Other:(", o.x, o.is_st, o.ht,")")
        if self.x != o.x:
            #print("x is not same. return", self.x - o.x)
            return (self.x - o.x < 0)
        else:

            if self.is_st and o.is_st:
                # Return True if self is higher otherwise return False
                # so that other can be picked first
                return self.ht > o.ht

            if not self.is_st and not o.is_st:
                # Return True if self is lower otherwise return False
                # so that other can be picked first
                return self.ht < o.ht

            # Incase one is start and other is end, the one which is
            # 'Start' should be picked up first
            if self.is_st:
                # Picking self
                return True
            else:
                # Picking other
                return False

#            if self.is_st:
#                h1 = -self.ht
#            else:
#                h1 = self.ht
#
#            if o.is_st:
#                h2 = -o.ht
#            else:
#                h2 = o.ht
#
#            return (h1 - h2 < 0)

    def __gt__(self, o):
        print("gt:")
        return -(self.__lt__(o))

    def __ge_(self, o):
        print("ge:")

    def __le_(self, o):
        print("le:")

    def __eq__(self, o):
        print("eq:")
        return 0

def print_bld(l):
    #while l:
    for pt in l:
        #x, is_st, ht = heappop(l)
        #pt = heappop(l)
        print("x:", pt.x,", is_st:", pt.is_st, ", ht:", pt.ht)

#b01 = Bld_point(1, 0, 3)
#b02 = Bld_point(4, 1, 3)
#b11 = Bld_point(2, 0, 4)
#b12 = Bld_point(4, 1, 4)

#points = [(2, 9, 10), (2, 7, 12), (3, 7, 15), (5, 12, 12), (15, 20, 10), (19, 24, 8)]
points = [(2, 9, 10), (3, 7, 15), (5, 12, 12), (15, 20, 10), (19, 24, 8)]
#points = [(2, 9, 10)]

#p1 = []
#for x, y, ht in points:
#    p1.append(Bld_point(x, 1, ht))
#    p1.append(Bld_point(y, 0, ht))
#
#p1 = sorted(p1)
#print_bld(p1)
#exit()

l = []
for x, y, ht in points:
    heappush(l, Bld_point(x, 1, ht))
    heappush(l, Bld_point(y, 0, ht))

#print_bld(l)

max_pq = []
ht_count_map = {}

def add_height(ht):
    if ht in ht_count_map:
        update_height(ht)
        return

    entry = [-ht, 1]
    heappush(max_pq, entry)
    ht_count_map[ht] = entry

def update_height(ht):
    entry = ht_count_map[ht]
    entry[1] += 1

def print_list(l):
    for n in l:
        print(n, ", id:", hex(id(n)), end =" ")
    print()

def print_map(h):
    print("{ ")
    for n in h:
        print(n, ":", h[n], ", id:", hex(id(h[n])), end =" ")
    print("}")


def remove_height(ht):
    if ht not in ht_count_map:
        print("===============ht:", ht," not found")
        return

    entry = ht_count_map[ht]
    if entry[1] == 1:
        last_entry = max_pq[-1]
        #print("ht_count_map:", ht_count_map)
        #print("last_entry:[", last_entry[0], last_entry[1])
        #print("entry:[", entry[0],entry[1], ", id:", hex(id(entry)))
        entry[0] = last_entry[0]
        entry[1] = last_entry[1]
        #print("entry:[", entry[0],entry[1], ", id:", hex(id(entry)))
        #print("before ht:", ht, ", max_pq:", print_list(max_pq))
        max_pq.pop(-1)
        #print("removing ht:", ht, ", max_pq:", print_list(max_pq))
        heapify(max_pq)

        ht_count_map.pop(ht)
        ht_count_map[-last_entry[0]] = entry

        #print("ht_count_map:", ht_count_map)
        return

    entry[1] -= 1
    #return([-entry[0], entry[1])

#add_height(0)
#print(max_pq)
#add_height(0)
#print(max_pq)
#add_height(0)
#print(max_pq)
#remove_height(0)
#print(max_pq)
#remove_height(0)
#print(max_pq)
#remove_height(0)
#print(max_pq)
#remove_height(0)
#print(max_pq)

max_ht = 0
ans = []
add_height(0) # count 1

count = 0

while l:
   
    bld_pt = heappop(l)
    #print("=============")
    #print("x:", bld_pt.x, ", is_st:", bld_pt.is_st, ", ht:", bld_pt.ht)
    #print("max_pq:", max_pq)

    if bld_pt.is_st:
        add_height(bld_pt.ht)

        if max_ht < bld_pt.ht:
            ans.append([bld_pt.x, bld_pt.ht])
            max_ht = bld_pt.ht
    else:
        remove_height(bld_pt.ht)

        if max_ht == bld_pt.ht:
            # This means max_ht may need to be updated as bld_pt.ht is
            # going out.
            cur_top_ht, count = max_pq[0] # peek API is needed here.
            cur_top_ht = -cur_top_ht

            if max_ht != cur_top_ht:
                ans.append([bld_pt.x, cur_top_ht])

            max_ht = cur_top_ht

    #print(".")
    #print("max_pq:", max_pq)
    #print("max_ht:", max_ht)
    #print("ans:", ans)

#print("========= Over ============")
#print_bld(l)
#print(max_pq)
#print(l)
print(ans)

