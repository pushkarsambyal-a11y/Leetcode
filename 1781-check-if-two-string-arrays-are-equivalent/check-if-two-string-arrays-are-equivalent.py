class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        s = "".join(word1)
        t = "".join(word2)

        if s == t:
            return True
        else:
            return False
       
        