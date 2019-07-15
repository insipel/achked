#!/usr/bin/env python3

from collections import *

def max_sliding(l, w):
    n = len(l)
    ans = [0] * (n - w + 1)
    #ans = []

    # Stores the indices of the elements. It serves 2 purposes. One
    # that we can check the sliding window size and we can get the
    # list number at this index as well.
    dq = deque()

    for i in range(n):
        num = l[i]

        while dq and l[dq[-1]] <= num:
            dq.pop()
        dq.append(i)
        #print(dq)

        if i >= w - 1:
            #print("i - w:", i - w)
            while dq[0] <= i - w: # not i - w + 1
                #print("popping:", dq[0])
                dq.popleft()
            #print("after pop:", dq)

            ans[i - w + 1] = l[dq[0]]
            #ans.append(l[dq[0]])
            #print("ans:", ans)

    print(ans)



l = [2, 3, 1, -3, 5, 3, 6, 7]
w = 3
print(l)
max_sliding(l, w)

