#!/usr/bin/env python3

def next(a, i):
    return a[i]

def find_dup_working(A):
    slow = A[0]
    #fast = A[A[0]] if we don't do it, then we can get into a lock step
    fast = A[A[0]]
    
    # Phase1: Take 2 pointers slow and fast. Fast moves with double
    # the speed of slow. If there is a cycle the two pointers will
    # meet somewhere.
    while slow != fast:
        slow = A[slow]
        fast = A[A[fast]]

    #  Phase2: Keep the fast pointer where it is. Move the slow
    #  pointer to the start of the linked list. Now advance both the
    #  pointers at the same speed. The point where they meet is the
    #  start node of a loop.  In our case, that is our duplicate
    #  node.
    fast = 0
    while (slow != fast):
        slow = A[slow]
        fast = A[fast]

    return slow







def loop_head(a, cur):
    slow = len(a) - 1
    fast = cur

    break_cnt=6
    while slow != fast:
        print("slow:", slow, ", fast:", fast)
        slow = next(a, slow)
        fast = next(a, fast)
        break_cnt-=1
        if not break_cnt:
            break;
    print("Duplicate elem:", a[slow])

def find_dup(a):
    head = len(a) - 1
    n = len(a)

    slow = head
    fast = next(a, slow)

    print("slow:", slow, "a[slow]:", a[slow], "fast:", fast, "a[fast]:", a[fast])
    while slow != fast:
        slow = next(a, slow)
        fast = next(a, next(a, fast))
        print("slow:", slow, "a[slow]:", a[slow], "fast:", fast, "a[fast]:", a[fast])

    print("Going for loop_head: slow:", slow, "a[slow]:", a[slow])
    loop_head(a, slow)

def find_dup_simple(l):
    n = len(l)
    res = []

    for i in range(n):
        print(l)
        idx = abs(l[i])
        num = l[idx]

        if num == 0:
            l[idx] = -n
        elif num < 0:
            res.append(abs(l[i]))
        else:
            l[idx] = -num

    print("duplicates are: ", res)

def main():
    print("Find duplicates")
    #a = [4, 2, 1, 4, 3, 2]
    #a = [4, 5, 1, 4, 3, 2]
    #a = [2, 1, 5, 4, 3, 4]
    #a = [4] INCORRECT INPUT. DOESN"T MATCH PROBLEM DEF no dup in this size
    #a = [4,1]
    #a = [1,1]
    #find_dup(a)
    #print(find_dup_working(a))
    a = [0, 1, 0, 3, 3]
    find_dup_simple(a)

main()

###
# question to ask:
#    1. what guaratees that there is a loop
#    2. eg 4 4 1 2 3 2
#    index 0 1 2 3 4 5, range: 0-4, n = 5
#     if you draw the linking, then you would see that slow and fast
#     pointers would meet at index 4,  
