import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def k_check(k, piles, h):
            time = 0
            for x in piles:
                time += math.ceil(x / k)
            
            if time <= h:
                return k
            else:
                return False

        k = max(piles)
        low, high = 1, k

        while low <= high:
            mid_k = (high+low) // 2

            k_tocheck = k_check(mid_k, piles, h)

            if k_tocheck != False:
                k = min(mid_k, k_tocheck)
                high = mid_k - 1
            
            else:
                low = mid_k + 1

        return k 
        
