class Solution(object):
    def containsDuplicate(self, nums):
        n = set(nums)
        if len(nums) != len(n):
            return True
        else:
            return False
      