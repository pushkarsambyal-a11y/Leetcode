class Solution(object):
    def twoSum(self, nums, target):
        n = {}
        found = False

        for i in range(len(nums)):
            num = nums[i]
            need = target - num

            if need in n:
                return n[need], i
                found = True
                break
            n[num] = i

        if not found:
            return -1


        

        