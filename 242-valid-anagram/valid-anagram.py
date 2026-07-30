class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        else:
            count = {}

            for char in s:
                if char in count:
                    count[char] += 1
                else:
                    count[char] = 1
                
            valid = True
            for char in t:
                if char not in count or count[char] == 0:
                    valid = False
                    break
                count[char] -= 1
        if valid:
            return True
        else:
            return False
            
        