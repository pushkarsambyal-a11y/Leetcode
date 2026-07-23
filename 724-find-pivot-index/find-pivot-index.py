class Solution(object):
    def pivotIndex(self, nums):
        left_sum = 0
        count = 0
        total = sum(nums)

        for idx, val in enumerate(nums):
            right_sum = total - left_sum - val
            if left_sum == right_sum:
                return idx
            left_sum += val 
        return -1