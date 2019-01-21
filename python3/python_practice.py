#!/usr/bin/env python3

#from random import randint
import random

var1, var2, var3 = 3, 9,10
print(var1)
print(var1,var2,var3)

print(var1,end='')
print(var2,end='')
print(var3)

for num in range(1,3):
    print(num,end='')

print()

def run_cmd():
    l = []
    #N = int(input())
    #12
    cmd_list = [ "12",
                 "insert 0 5", "insert 1 10", "insert 0 6", "print",
                 "remove 6", "append 9", "append 1", "sort", "print",
                 "pop", "reverse", "print"]
    N = int(cmd_list[0])

    for idx in range(1,N+1):
        #ip = input().split()
        ip = cmd_list[idx].split()
        cmd = ip[0]
        cmd1 = ip[1:]
        if cmd == 'print':
            print(l)
        else:
            cmd += "(" + ",".join(cmd1) + ")"
            eval("l."+cmd)
#run_cmd()

n = 6
nums = list(random.randint(0,100) for _ in range(n))
nums1 = map(int, nums) #map is same as above
print(nums)
print("mapped", list(nums1))

# coverting list to tuple, hash only works on immutable objects
# tuple is immutable, only can be added, accessed like
# a = tuple() --  { a : 1 } like a dict
num_tuple = tuple(nums)
print(num_tuple)


x = y = z = 3
n = 2
l = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in \
        range(z+1) if (i+j+k != n)]
#print(l)

l = [2,3,6,6,5]
#lset = set(l)
#l = [x for x in lset]
#l.sort()
max1 = -101
max2 = -101
for num in l:
    if (num > max2 and num < max1):
        max2 = num

    if (num > max1):
        max2 = max1
        max1 = num

print(max2)


names = []
scores = []
names.append('harry')
scores.append(37.21)
names.append('Berry')
scores.append(37.21)
names.append('Tina')
scores.append(37.2)
names.append('Akriti')
scores.append(41)
names.append('Harsh')
scores.append(39)

names_scores = list(zip(names, scores))
lowest2 = sorted(list(set(scores)))[1]
print(lowest2)
print(names_scores)

print('\n'.join(name for name,score in sorted(names_scores) if score == lowest2))

