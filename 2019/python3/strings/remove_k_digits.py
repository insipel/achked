#!/usr/bin/env python3

'''
In the class, a look back on k+1 digits was discussed. There is a lot of index
manipulation in that approach. Stack based approach is much simpler.
'''
def remove_k_digits(num: str, digits_to_remove: int) -> str:
    stack = []
    
    for digit in num:
        # While we still have allowed removals, the stack isn't empty,
        # and the last digit in the stack is greater than the current digit,
        # pop the larger digit to maintain the smallest lexicographical order.
        while digits_to_remove > 0 and stack and stack[-1] > digit:
            stack.pop()
            digits_to_remove -= 1
        stack.append(digit)
        
    # If we still have remaining removals (e.g., the number was strictly increasing),
    # drop the excess digits from the end of the stack.
    if digits_to_remove > 0:
        stack = stack[:-digits_to_remove]
        
    # Join the stack into a string and strip any leading zeros.
    result = "".join(stack).lstrip('0')
    
    # Return "0" if the resulting string is empty.
    return result if result else "0"

# Example usage:
number = "1432219"
removals = 3
print(f"Original: {number}, Removals allowed: {removals}")
print(f"Result: {remove_k_digits(number, removals)}")  # Output: "1219"
num = 31243819
digits_to_remove = 3
print(remove_k_digits(str(num), digits_to_remove))
