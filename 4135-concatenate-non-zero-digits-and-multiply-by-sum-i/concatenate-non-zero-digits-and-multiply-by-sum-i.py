class Solution(object):
    def sumAndMultiply(self, n):
        n_sum = 0
        s = str(n)
        lst = []
        for i in s :
            if i!="0":
                lst.append(int(i))
        if not lst:
            return 0
        su=sum(lst)
        x = int("".join(map(str, lst)))

        return x*su        
        


       
            
        