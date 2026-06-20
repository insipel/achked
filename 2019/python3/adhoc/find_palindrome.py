#!/usr/bin/env python3

def convert(num):
    digits = []
    while num:
        digits.append(num%10)
        num = int(num/10)

    return digits[::-1]

def all9s(num):
    for i in num:
        if i != 9:
            return False
    return True

def find_palindrome(num):
    digits = convert(num)
    print(digits)
    output = []

    if all9s(digits):
        output.append(1)
        for i in range(1, len(digits)):
            output.append(0)
        output.append(1)
        #return output[::-1]
        return output

    else:
        pass

#num = 713322
num = 99999
print(find_palindrome(num))

