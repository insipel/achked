#!/usr/bin/env python3

def smallest_number_after_removing_k_digits(number, k):

    #Get the number in array format
    numbers = [int(x) for x in str(number)]

    #Guards
    if len(numbers) <= k: # AP: change here to =
        return -1
    if k == 0:
        return number

    #Handle an edge case here. If numbers are in
    #strictly increasing order, just drop last k
    if numbers == sorted(numbers):
        return int(''.join([str(x) for x in numbers[:len(numbers)-k]]))    
   
    #Set the window to be k+1 in size
    left_idx, right_idx = 0, k

    #Move the window till end of the string
    while right_idx < len(numbers) + 1:

        window = numbers[left_idx : right_idx]

        #Find the position of the smallest number
        #If there are dupes, find the leftmost
        smallest_idx = window.index(min(window))

        #Drop all numbers to the left of the smallest
        numbers = numbers[:left_idx] + numbers[left_idx + smallest_idx:]

        #But, if the smallest index is the very first, the window still needs to move
        if smallest_idx == 0:
            left_idx += 1
            right_idx += 1
        #Now calculate how much right has to go fwd, to maintain window size
        else:
            #diff = (k + 1) - len(window)
            diff = (smallest_idx - left_idx)
            right_idx += diff
            left_idx = left_idx + smallest_idx
 
    print(numbers, left_idx, right_idx)
    return  int(''.join([str(x) for x in numbers]))

num = 31243819
window = 3
print(smallest_number_after_removing_k_digits(num, window))

def remove_digits(s, st, n, res):
    print("s:", s, ", st:", st, ", n:", n, ", res", res)

    if n == 0:
        print("n is 0 now")
        res.append(s[st:])
        return

    left_s = len(s) - st - 1
    if left_s <=n:
        print("left_s:", left_s, "n: ", n)
        return

    min_idx = st
    for i in range(st+1, len(s)):
        if s[min_idx] > s[i]:
            min_idx = i
            n = n -1

    print("min_idx: ", min_idx)
    print("res:", res)
    res.append(s[min_idx])
    remove_digits(s, min_idx+1, n, res)

res = []
#remove_digits(str(num), 0, window-1, res)
#print(res)





def get_smallest(s, st, w):
    d = s[st]
    idx = st

    for i in range(st+1, st+w+1):
        if s[i] < d:
            d = s[i]
            idx = i
    print("get_smallest: digit", ord(d) - ord('0'), " at index:", idx)
    return ord(d) - ord('0'), idx

# Gets num representing all the digits starting at index i
def get_digits(s, idx):

    num = 0
    for i in range(idx, len(s)):
        num = num * 10 + (ord(s[i]) - ord('0'))

    print("get_digits: num", num)
    return num


def remove_k_digits(n, k):
    s = str(n)
    st, end, w = 0, len(s), k+1
    d = 0
    num = 0
    i = 0
    num_left_digits = 0
    removed = 0

    while (st+w) < end:

        # min_digit is the digit value at index 'i', num_left_digits
        # returns how many more digits are left in the str to scan.
        # which can be really derived from i. (end - i - 1)
        #min_digit, i, num_left_digits = get_smallest(s, st, w)
        d, i = get_smallest(s, st, w)
        removed += (i - st)
        num = num * 10 + d
        print("num so far:", num, ", removed:", removed)

        num_left_digits = end - (i  + 1)
        if num_left_digits < w:
            break

        st = i + 1


    if num_left_digits < w:
        num = num * (10 ** (k - num_left_digits)) + get_digits(s, i)
        print("num:", num)

    return num

num = 31243819
window = 3
#print(remove_k_digits(str(num), window))
