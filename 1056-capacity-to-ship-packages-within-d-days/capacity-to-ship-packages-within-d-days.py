class Solution(object):
    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = sum(weights)
        ans = high

        while low <= high:
            mid = (low + high)//2
            current_weight = 0
            n_days = 1
            for weight in weights:
                if current_weight + weight > mid:
                    n_days += 1
                    current_weight = weight
                else:
                    current_weight += weight
            
            if n_days <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
            
 
             
        