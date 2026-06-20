#!/usr/bin/env python3

def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

def permute(l, i):
    if i == len(l)-1:
        #print(''.join(c for c in l))
        print("".join(l))
        return

    for j in range(i, len(l)):
        swap(l, i, j)
        permute(l, i+1)
        swap(l, i, j)

def main():
    s="abc"
    #l = [c for c in s]
    l = list(s)
    permute(l, 0)

if __name__ == '__main__':
    main()

