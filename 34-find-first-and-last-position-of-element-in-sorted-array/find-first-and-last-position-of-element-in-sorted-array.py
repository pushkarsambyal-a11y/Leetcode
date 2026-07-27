class Solution(object):
    def searchRange(self, nums, target):
        if len(nums) == 0:
            print("-1, -1")
        
        ind1 = bisect.bisect_left(nums, target)
        ind2 = bisect.bisect_right(nums, target)

        if ind1 < len(nums) and nums[ind1] == target:
            return ind1, ind2 - 1
        else:
            return -1, -1


        