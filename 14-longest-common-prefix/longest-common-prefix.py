class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Iterate through the characters of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            # Check this character against the same position in all other strings
            for string in strs[1:]:
                # If the current string is shorter than 'i' or characters don't match
                if i == len(string) or string[i] != char:
                    return strs[0][:i]
                    
        return strs[0]
        
       
        