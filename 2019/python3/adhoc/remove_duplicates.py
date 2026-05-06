#!/usr/bin/env python3

# idea is to place each number at its right index in each iteration
def remove(l):
    n = len(l)
    for i in range(n):
        #print(l)
        if l[i] == i:
            continue
        else:
            cur = i
            nxt = l[i]

            # This will happen if a number is already placed at its
            # correct index previous and we encounter a new idx with
            # the same number (duplicate)
            # eg.  i: 0  1  2  3  4 . . .
            #         .  .  .  3  3 . . .
            # when i = 4, nxt = l[i] = 3
            # here if l[nxt] == l[i] (current element), then it means
            # that current element is a duplicate and can be
            # eliminated.
            if nxt == l[nxt]:
                l[cur] = -1
                continue

            while cur != -1 and cur != nxt:
                #print("cur:", cur, ", nxt:", nxt)
                new_nxt = l[nxt]
                l[nxt] = nxt

                cur = nxt
                nxt = new_nxt

def main():
    l = [3, 0, 4, 1, 4]
    remove(l)
    print(l)

if __name__ == "__main__":
    main()

