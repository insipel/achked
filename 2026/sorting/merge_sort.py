#!/usr/bin/env python3

class MergeSort:
    def __init__(self):
        pass

    def sort(self, nums):
        input_list = list(nums)
        self.merge_sort(nums, 0, len(nums)) # end here is exclusive bound
        print("[", *input_list, "]", "=>", "[", *nums, "]")
        print(f"[{', '.join(map(str, input_list))}] => [{', '.join(map(str, nums))}]")
        print(f"[{', '.join(map(str, input_list))}]")
        print(', '.join(map(str, input_list)))
    
    def merge_sort(self, nums, st, end): # end is 
        # because end is exclusive bound, 1 should be added to st to make it compare to end.
        if (end - st > 1):
            # print("Sorting: ", *nums[st:end])
            m = (st + end) // 2;
            self.merge_sort(nums, st, m)
            self.merge_sort(nums, m, end)
            self.merge(nums, st, m, end)
            # print("Merged: ", *nums[st:end])

    def merge(self, nums, st, m, end):
        list1 = nums[st:m]
        list2 = nums[m:end]
        # print("List 1: ", *list1)
        # print("List 2: ", *list2)
        
        i = st
        i1 = i2 = 0
        while i1 < len(list1) and i2 < len(list2):
            if list1[i1] < list2[i2]:
                nums[i] = list1[i1]
                i1 = i1+1
            else: # list1[i1] >= list2[i2]
                nums[i] = list2[i2]
                i2 = i2+1
            i = i+1
        
        while i1 < len(list1):
            nums[i] = list1[i1]
            i += 1
            i1 += 1

        while i2 < len(list2):
            nums[i] = list2[i2]
            i += 1
            i2 += 1



numbers = [[1, 67, 23, 98, 12, -5, 0], [0], [], [-5], [1, 6], [12, 9], [4, 9, 0, 23]]
obj = MergeSort()
for nums in numbers:
    obj.sort(nums)