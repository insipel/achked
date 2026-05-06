#!/usr/bin/env python3


def generate_all_expressions(num, target):
    """
    :type num: str
    :type target: int
    :rtype: List[str]
    """
    if not num:
        return []
    output = []

    def _dfs(so_far, evaluated, idx, prev):
        """
        :param so_far: expression so far (string)
        :param evaluated: evaluated value so far (int)
        :param idx: index to start recursing from
        :param prev: prev value to use for the multiplication special case to give it precedence
        :return: doesn't return, appends to output in the base case
        """
        if idx == len(num):
            if evaluated == target:
                output.append(so_far)
            return

        for i in range(idx, len(num)):
            # For an input like 1234, depending on idx, curr will be
            # 1, 12, 123, 1234; 2 23 234; 3 34; 4 (all possible splits)
            # Note that only 1, 12, 123 and 1234 will be considered
            # for the case when 'idx == 0' is true.

            # This takes care of the concat case as concat has most precedence
            curr = num[idx:i+1]
            curr_int = int(curr)

            if idx == 0:

                # just appending digits for this pass
                # this can be outside the recursive function before dfs is called, but having it here makes
                # it more DRY since we will have to do the curr and curr_int outside otherwise for 1234 case,
                #   when idx = 0, we will have 1, 12, 123, 1234
                # prev value is just current_int (which is same as evaluated)

                #print("1:", curr, ", i:", i, ", curr_int:",
                #        curr_int)
                _dfs(so_far + curr, curr_int, i+1, curr_int)
                # or _dfs(curr, curr_int, i+1, curr_int) since so_far
                # is "" anyways.

            else:
                #print("2:")
                _dfs(so_far + '+' + curr, evaluated+curr_int, i+1, curr_int)

                # Notice the prev value here as -curr_int
                _dfs(so_far + '-' + curr, evaluated-curr_int, i+1, -curr_int)
                #print("3:")
                _dfs(so_far + '*' + curr, (evaluated-prev) + (prev*curr_int), i+1, prev*curr_int)

    _dfs('', 0, 0, 0)
    return output

print("Target:19", generate_all_expressions('1234', 19))
print("Target:24", generate_all_expressions('1234', 24))
print("Target:21", generate_all_expressions('1234', 21))
print("Target:5", generate_all_expressions('1234', 5))
print("Target:20", generate_all_expressions('1234', 20))
