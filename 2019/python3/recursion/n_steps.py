#!/usr/bin/env python3

# DP code is not producing correct output
# recursion is good.

def countWaysToClimb(steps, n):
    if n < steps[0]:
        return 0
        
    #for step in steps:
    #    if n == step:
    #        return 1
    
    total = 0
    for i in range(len(steps)):
        if n == steps[i]:
            total += 1
            continue
        total += countWaysToClimb(steps, n - steps[i])
    
    return total

def countWaysToClimb_dp(steps, n):
    s = [0] * (n + 1)
    
    for i in range(n+1):
        for step in steps:
            if i < step:
                continue
            if i == step:
                s[i] = 1
                continue
            s[i] += s[i - step]
            
    return s[n]

def simple_climb(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    return simple_climb(n-1) + simple_climb(n-2)

def main():
    #print(countWaysToClimb_dp([2,3], 7))
    n = 4
    print(countWaysToClimb([1,2], n))
    print(countWaysToClimb_dp([1,2], n))
    print(simple_climb(n))

if __name__ == '__main__':
    main()

