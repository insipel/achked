#!/usr/bin/env python3

def next(a, i):
    return a[i]

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

    print("slow:", slow, "a[slow]:", a[slow])
    loop_head(a, slow)


def main():
    print("Find duplicates")
    #a = [4, 2, 1, 4, 3, 2]
    a = [4, 4, 1, 2, 3, 2]
    #a = [4] no dup in this size
    #a = [4,1]
    #a = [1,1]
    find_dup(a)

main()

###
# question to ask:
#    1. what guaratees that there is a loop
#    2. eg 4 4 1 2 3 2
#    index 0 1 2 3 4 5, range: 0-4, n = 5
#     if you draw the linking, then you would see that slow and fast
#     pointers would meet at index 4,  
