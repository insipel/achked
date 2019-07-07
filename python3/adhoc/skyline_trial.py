def max_building_volume(left, front):
    left = sorted(left)
    front = sorted(front)
    i = 0
    sum_to_ith = 0 # prefix sum of 0 to ith building in current row up
    total = 0 #total volume
    for h in left:
        while i < len(front) and h >= front[i]:
            sum_to_ith += front[i]
            i += 1
            total += (sum_to_ith + (len(front) - i) * h)
    return total

https://aonecode.com/google-interview-questions/maximum-block-volume









