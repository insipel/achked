#!/usr/bin/env python3

def insertion_sort(l):

    for i in range(len(l)):
        key = l[i]
        j = i
        while j > 0:
            if l[j - 1] > key:
                l[j] = l[j - 1]
                j -= 1
            else:
                break
        l[j] = key

def main():
    l = [4, 3, 45, 2, 22, 15, 6, 22, 19, 18, 27]
    insertion_sort(l)
    print(l)

if __name__ == '__main__':
    main()

