#!/usr/bin/env python3

# Runtime: O(Catalan_number(n)). Grows very fast.
# for n=35, it's 100K Trillion.
def num_bsts_rec(n):
    if n <= 1:
        return 1

    count = 0
    for i in range(n):
        count += num_bsts_rec(i) * num_bsts_rec(n - 1 - i)

    return count

# Runtime: O(n^2)
def num_bsts_memo(n, memo):
    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = 1
        return 1

    count = 0
    for i in range(n):
        count += num_bsts_memo(i, memo) * num_bsts_memo(n - 1 - i, memo)

    memo[n] = count

    return count

def num_bsts_iter(n):
    # RR: is f(n) = sum(f(i) * f(n - i -1)) for all values of i
    # The second function is going 1 less than 0 since we need n+1
    # cells in our table.
    #num_bsts = [0] * n+1 ====> This errors out.
    num_bsts = [0] * (n+1)
    num_bsts[0] = 1

    for cur_bst_sz in range(1, n+1):

        for num_left_nodes in range(0,cur_bst_sz):

            num_right_nodes = cur_bst_sz - 1 - num_left_nodes
            num_bsts[cur_bst_sz] += num_bsts[num_left_nodes] * num_bsts[num_right_nodes]

    return num_bsts[n]

for i in range(1, 10):
    print("#nodes:", i, ", num BSTs:", num_bsts_rec(i))
    print("#nodes:", i, ", num BSTs:", num_bsts_memo(i, {}))
    print("#nodes:", i, ", num BSTs:", num_bsts_iter(i))