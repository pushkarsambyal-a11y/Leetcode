class Solution(object):
    def maxDistance(self, arr, m):
        arr.sort()
        low = 1
        high = arr[-1] - arr[0]
        ans = high

        while low <= high:
            mid = (low + high)//2
            ball_place = 1
            last_ball = arr[0]

            for i in arr:
                if i - last_ball >= mid:
                    ball_place += 1
                    last_ball = i
            if ball_place >= m:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
        