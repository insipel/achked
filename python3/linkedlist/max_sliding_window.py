#!/usr/bin/env python3

from collections import *

def max_sliding(l, window_sz):
    n = len(l)
    ans = [0] * (n - window_sz + 1)
    #ans = []

    # Stores the indices of the elements. It serves 2 purposes. One
    # that we can check the sliding window size and we can get the
    # list number at this index as well.
    dq = deque()

    #for i in range(n):
    for cur_idx in range(n):
        num = l[cur_idx]

        if dq:
            last_idx = dq[-1]

        while dq and l[last_idx] <= num:
            dq.pop()
            if dq: last_idx = dq[-1]

        dq.append(cur_idx)
        #print(dq)

        if cur_idx >= window_sz - 1:
            #print("cur_idx - window_sz:", cur_idx - window_sz)
            top_idx = dq[0]

            # removing the elements not in the sliding window
            while top_idx <= cur_idx - window_sz: # not cur_idx - window_sz + 1
                #print("popping:", dq[0])
                dq.popleft()
                top_idx = dq[0]

            #print("after pop:", dq)

            #ans[cur_idx - window_sz + 1] = l[dq[0]]
            # cur_idx: 2, win: 3, so writing at 0th index
            ans[cur_idx - window_sz + 1] = l[top_idx]
            #ans.append(l[dq[0]])
            #print("ans:", ans)

    print(ans)



l = [2, 3, 1, -3, 5, 3, 6, 7]
w = 3
print(l)
max_sliding(l, w)

