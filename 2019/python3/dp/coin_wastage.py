'''
You want to buy an item that costs some amount from a vending machine that doesn't give change.
Given some possible bill sizes, find the minimum amount of money you can waste.

amount = A
bills = B as []

f(a, B): returns the min amount of money that'll be wasted to reach sum 'a'

f(a, B):
1.   0   if a == 0
2.  (B[i] - a)  if a < B[i] for all i
3. min (abs(f(a - B[i], B), abs(a - B[i])) for i

A = 10
B = 3, 4, 5
Ans: 0

A = 14, 5, 6, 7
B = 4, 8
Ans: 2, 3, 2, 1

B = 4, 8
i: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 
r: 0, 3, 2, 1, 0, 3, 2, 1, 0, 1,  2,  1,  





min ( A % B[i]) for i


A = 45
B = [20, 30]
residual: 5, 15
wastage for counting to sum of 5, 15
                              15,  5
                              
A = 133
B = [42, 45, 46]
residual:   7 , 43 , 41
wastage:   35 (bill: 42),  2,  1


            133
   91        88            87
a, b, c    a1,b1,c1      a2,b2,c2
49 46 45   48 43 42
7 4 3
-35


for b in Bills:
    if a > b:
        min_wastage(a - b)
  
'''
