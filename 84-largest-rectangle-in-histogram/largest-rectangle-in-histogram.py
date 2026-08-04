class Solution(object):
    def largestRectangleArea(self, heights):
        n = len(heights)
        nse = [n] * n
        st = []

        for i in range(n-1, -1, -1):
            while len(st) > 0 and heights[st[-1]] >= heights[i]:
                st.pop()
            if len(st) > 0:
                nse[i] = st[-1]
            st.append(i)
        
        del st[:]
        pse = [-1] * n

        for i in range(0, n):
            while len(st) > 0 and heights[st[-1]] >= heights[i]:
                st.pop()
            if len(st) > 0:
                pse[i] = st[-1]
            st.append(i)

        ans = 0
        for i in range(n):
            width = nse[i] - pse[i] - 1
            area = heights[i] * width
            ans = max(ans, area)
        return ans


            
        