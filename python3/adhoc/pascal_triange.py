#!/usr/bin/env python3

import inspect

# Sum of the binomial coefficients
# The formula
#    for k = 0-n ∑ nCk = 2 ** n 
# says the elements in the nth row of Pascal's triangle always
# add up to 2 raised to the nth power
#
# The problem asks to report the
#   F(array) = Summation over all i ( Summation over all j (
#                           (i+1)*array[i][j] + (j+1) ) ) % (10^9 + 7),
#                                               where 0<=i<n and 0<=j<=i
#
#   This in other words is
#   F(array) = Sum of the row * row_idx + sum of total number of elems in a row
#           Sum of the row in sum of all binomial coefficient is (2 ** n)
#   that translates to
#       F(array) = n * (2 ** n) + (n * (n + 1))/2
def findFofPascalTriangle(n):
    #
    # Write your code here.
    #
    i = 0
    f = 0
    
    while i < n:
        # We want to use i as 1, 2, 3. so use (i + 1) in the next formula
        # sum of j + 1 is also using 1, 2, 3 i.e j+1, so the sum of
        # all natual numbers from 1 to n uses (j +1) as n. jth row has
        # (j + 1) elements
        f += (i + 1) * (2 ** i) + (i + 1) * (2 + i) // 2
        i += 1
    return(f % (10**9 + 7))


def total_pt_formula(n):
    target = 0
    i = 1
    #for i in range(1, n+1):
    while i < n + 1:
        target += i * (2 ** (i - 1)) + (i * (i + 1))//2
        i+=1

    return target % (10 ** 9 + 7)

def total_pt(n):
    cur_list = [1]
    total = 2
    print("1")

    for i in range(1,n):
        k = 0
        cur_len = len(cur_list)

        nxt_list = [1]
        k+=1
        total = (total + ((i+1) * 1 + k))
        print("1", end=' ')

        for j in range(cur_len - 1):
            nxt_sum = cur_list[j] + cur_list[j+1]

            nxt_list.append(nxt_sum)
            k+=1
            total = (total + ((i+1) * nxt_sum + k))
            print(nxt_sum, end=' ')

        nxt_list.append(1)
        k+=1
        total = (total + ((i+1) * 1 + k)) % (10 ** 9 + 7)
        print("1")

        cur_list = nxt_list

    print("n:", n, ", total:", total)

def main():
    #PrintFrame()
    #print("Running pascal triangle total")
    #for i in range(1,7):
    #    total_pt(i)
    #    findFofPascalTriangle(i)
    #findFofPascalTriangle(10000)
    total_pt_formula(10000)

def PrintFrame():
  callerframerecord = inspect.stack()[1]    # 0 represents this line
                                            # 1 represents line at caller
  frame = callerframerecord[0]
  info = inspect.getframeinfo(frame)
  print(info.filename)                      # __FILE__     -> Test.py
  print(info.function)                      # __FUNCTION__ -> Main
  print(info.lineno)

main()
