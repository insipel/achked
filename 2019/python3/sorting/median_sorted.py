#!/usr/bin/env python3

# This function finds the median of two sorted arrays using binary search.
#    the median is computed as if the two sorted arrays were merged into one combined sorted array.
# It partitions the arrays to find the correct split point where the median lies.
# Time complexity: O(log(min(n, m))) where n and m are the lengths of the arrays.
def find_median(l1, l2):
    len1 = len(l1)
    len2 = len(l2)

    # Ensure l1 is the smaller array for efficiency (optional optimization)
    #if len1 > len2:
    #    return find_median(l2, l1)

    # Binary search on the smaller array (l1)
    st = 0
    end = len1

    # The goal is to find the median (middle element(s)) of the combined sorted array
    # without merging the two arrays, by partitioning them correctly.
    while st <= end:
        # Partition l1 at index1, and l2 at index2 such that left partitions have equal elements
        index1 = (st + end) // 2
        index2 = (len1 + len2 + 1) // 2 - index1
        # The line above as index2 = (len1 + len2 + 1) // 2 - index1 vs 
        #                   index2 = (len1 + len2) // 2 - index1,
        # They are not equivalent when the total length is odd — that's precisely when the +1 matters.
        #
        # The +1 is a ceiling trick: (len1 + len2 + 1) // 2 always gives ceil((len1+len2)/2). For even totals, ceil and floor are the same, so both formulas agree. For odd totals they differ by 1.
        # 
        # Why it matters: The +1 ensures the left partition gets the extra element when the total is odd. That's what makes return max(max_left1, max_left2) on line 47 correct — the median lives in the max of the left half only if the left half is the larger one.
        # 
        # Concrete example: l1 = [1, 3], l2 = [2], total = 3 (odd), median = 2.
        # 
        # At index1 = 1:
        # 
        # Formula	index2	max_left1	max_left2	result
        # with +1	    1	        1	        2	max(1,2) = 2 ✓
        # without +1	0	        1	     -inf	max(1,-inf) = 1 ✗
        # Without +1, you'd need to change line 47 to return min(min_right1, min_right2) to get the right answer — the two formulas just put the median on opposite sides of the partition.


        # Get the boundary elements for the partitions
        max_left1 = l1[index1 - 1] if index1 != 0 else float('-inf')  # Max in left half of l1
        min_right1 = l1[index1] if index1 != len1 else float('inf')   # Min in right half of l1

        max_left2 = l2[index2 - 1] if index2 != 0 else float('-inf')  # Max in left half of l2
        min_right2 = l2[index2] if index2 != len2 else float('inf')   # Min in right half of l2

        # Debug prints to show current partition
        print("st:", st, ", end:", end)
        print("index1:", index1, ", index2:", index2)
        print("max_left1:", max_left1, ", min_right1:", min_right1, 
              ", max_left2:", max_left2, ", min_right2:", min_right2)

        # Check if the partition is correct: all left <= all right
        if max_left1 <= min_right2 and max_left2 <= min_right1:
            # Found the correct partition, compute median
            if ((len1 + len2) % 2 == 0):
                # Even total elements: average of the two middle elements
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            else:
                # Odd total elements: the middle element is the max of left halves
                return max(max_left1, max_left2)
        elif max_left1 < min_right2: # ie. max_left2 > min_right1
            # max_left2 is greater than min_right1. index1 is not partitioning to
            # find the middle of the array.
            # Too few elements in left of l1, move partition right
            st = index1 + 1
        else:
            # max_left1 > min_right2 means that max_left1 will appear after min_right2
            # if both the arrays were sorted and merged in a single array. This means
            # that the element contributing to the median will be before 
            # max_left1 in the first array, l1. Hence setting the end to index1 - 1 will
            # force the binary search to work on the left portion of l1.
            # IOW, the left portion of l1 has too many elements
            end = index1 - 1

    return -1  # Should not reach here if inputs are valid

def main():
    # Example test cases
    #l1 = [1]
    #l2 = [4, 5, 6, 8, 10, 13, 14]
    l1 = [6, 15, 19]
    l2 = [2, 4, 5, 7, 11]
    #print(find_median(l1, l2))
    print(find_median(l2, l1))  # Note: swapping arrays to test symmetry

if __name__ == "__main__":
    main()

