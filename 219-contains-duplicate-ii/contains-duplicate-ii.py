class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        found = False

        for i in range(len(nums)):
            num = nums[i]

            if num in seen and i - seen[num] <= k:
                found = True
                break
            seen[num] = i

        if found:
            return True
        else:
            return False
         