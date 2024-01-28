def SubArrSum(a, size):
    max_so_far = a[0]
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum sum of contiguous subarray :", SubArrSum(nums,len(nums)))
