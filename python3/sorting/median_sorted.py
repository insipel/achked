#!/usr/bin/env python3

def find_median(l1, l2):
    len1 = len(l1)
    len2 = len(l2)

    if len1 > len2:
        return find_median(l2, l1)

    st = 0
    end = len1

    while st <= end:
        index1 = (st + end)//2
        index2 = (len1 + len2 + 1)//2 - index1

        max_left1 = l1[index1 - 1] if index1 != 0 else float('-inf')
        min_right1 = l1[index1] if index1 != len1 else float('inf')

        max_left2 = l2[index2 - 1] if index2 != 0 else float('-inf')
        min_right2 = l2[index2] if index2 != len2 else float('inf')

        print("st:", st, ", end:", end)
        print("index1:", index1, ", index2:", index2)
        print("max_left1:", max_left1, ", min_right1:", min_right1, 
              ", max_left2:", max_left2, ", min_right2:", min_right2)

        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if ((len1 + len2) % 2 == 0):
                return (max(max_left1, max_left2) +
                        min(min_right1, min_right2))/2
            else:
                return (max(max_left1, max_left2))
        elif max_left1 < min_right2:
            st = index1 + 1
        else:
            end = index1 - 1

    return -1

def main():
    #l1 = [1]
    #l2 = [ 4, 5, 6, 8, 10, 13, 14]
    l1 = [6, 15, 19]
    l2 = [ 2, 4, 5, 7, 11]
    #print(find_median(l1, l2))
    print(find_median(l2, l1))

if __name__ == "__main__":
    main()

