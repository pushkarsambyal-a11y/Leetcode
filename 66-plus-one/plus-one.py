class Solution(object):
    def plusOne(self, digits):
        num_str = "".join(map(str, digits))
        
        new_num = int(num_str) + 1
        
        return [int(d) for d in str(new_num)]
        