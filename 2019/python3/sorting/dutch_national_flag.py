#!/usr/bin/env python3

def swap(a, i , j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def dnf(a):
    st = 0
    end = len(a)

    i = st - 1
    j = st
    k = end

#    i       j            k
#Gs...| Bs... | ...??... | Rs ...
    while j < k:
        if a[j] == 'R':
            k = k - 1
            swap(a, k, j)
        elif a[j] == 'G':
            i = i + 1
            swap(a, i, j)
            j += 1
        else: # 'B'
            j += 1

def main():
    s = "GBRBBGGRRBGRGR"
    l = [c for c in s]
    dnf(l)
    print(l)

if __name__ == '__main__':
    main()

