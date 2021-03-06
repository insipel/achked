#!/usr/bin/env python3

def findMaxPossibleArea(h, l, r):
    s = []
    max_area = 0
    i = l
    
    while i < r:
        # if stack is not empty and current bar is higher than the
        # previous one, then push current bar in to the stack
        if (not s or h[s[-1]] <= h[i]):
            # keep on pushing to the stack when going up
            s.append(i)
            i += 1
        else:
            # if the stack has elements and cur bar is lower than
            # previous one, then need to pop. This is the case when we
            # are going down.
            #print("before pop:", s)
            top_idx = s[-1]
            s.pop()
            #print("after pop:", s)
            #print("top_idx:", top_idx)

            # if stack has elements, then it means that lower height
            # bars are seen before the top bar. so we need to
            # calculate the area from that lower bar to current one.
            # Thats what we are doing in (i - s[-1] -1 ).
            #
            # -1 is done because 'i' is already one past the number of
            # bars that should be included in the width calculation.
            # just uncomment the prints and run with the first input.
            #
            # if stack is empty after last pop (meaning there was just
            # one element in the stack), then it means that last_bar
            # was through and through (eg. 6,2,4,5,4,1) and hence we
            # are taking the width as cur_idx - 1 (-1 is not needed
            # since i is 0 based.
            width = (i - s[-1] - 1) if s else (i - l)
            # i - top_idx is better but doesn't work for hte first
            # testcase.

            area = width * h[top_idx]
            #print("i:", i, ", s[-1]:", s[-1] if s else -1 , ", area: ", area, ", width:", width, ", top_idx:",
            #        top_idx, ", h[top_idx]:", h[top_idx])
            max_area = max(max_area, area)
            
    # Now process the elements in the stack. It'll happen in cases
    # where we have ascending elements towards the end of the array.
    # eg 6,2,4,5,2,4,6,8. 2,4,6,8 will be left in the stack after the
    # previous while loop. so we are processing those elements.
    while s:
        top_idx = s[-1]
        s.pop()
        
        # This case is interesting. if s is not empty, then the
        # barrier is the previos element. e.g. 2, 4, 6, 8. if we are
        # processing 6, then we'd use this logic.
        # when we are processing the last elem in the stack, then that
        # should exists through and through. e.g. 2 in the above
        # example should range from start_idx 'l' to end_idx 'r'.
        #width = (r - s[-1]) if s else (r - l + 1)
        width = (r - top_idx) if s else (r - l)

        area = width * h[top_idx]
        max_area = max(max_area, area)
        
    return max_area

def main():
    #print("Find max area under histogram")
    h = [6, 2, 5, 4, 5, 1, 6]
    l = 0
    ##r = len(h) - 1
    r = len(h)
    print(h)
    print(findMaxPossibleArea(h, l, r))

    h = [6, 2, 4, 5, 4, 5, 4, 5, 1, 6]
    l = 0
    #r = len(h) - 1
    r = len(h)
    print(h)
    print(findMaxPossibleArea(h, l, r))

    h = [2, 4, 6, 5, 8]
    l = 0
    #r = len(h) - 1
    r = len(h)
    print(h)
    print(findMaxPossibleArea(h, l, r))

    h = [1, 1, 1, 10, 1, 1, 1]
    l = 0
    #r = len(h) - 1
    r = len(h)
    print(h)
    print(findMaxPossibleArea(h, l, r))

    h = [10, 10, 10, 10, 6, 10, 10, 10, 10]
    l = 0
    #r = len(h) - 1
    r = len(h)
    print(h)
    print(findMaxPossibleArea(h, l, r))

    h = [10, 3, 5, 7, 9, 2, 7, 9]
    l = 0
    #r = len(h) - 1
    r = len(h)
    print(h)
    print(findMaxPossibleArea(h, l, r))

    h = [10, 3, 5, 7, 9, 2, 4, 6, 8]
    l = 0
    #r = len(h) - 1
    r = len(h)
    print(h)
    print(findMaxPossibleArea(h, l, r))

    h = [4, 4, 4, 5]
    l = 0
    #r = len(h) - 1
    r = len(h)
    print(h)
    print(findMaxPossibleArea(h, l, r))

main()

