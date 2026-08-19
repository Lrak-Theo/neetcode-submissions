class Solution:
    def mySqrt(self, x: int) -> int:
        
        low = 0
        high = x 
        current = 0
        
        while low <= high:
            mid = (low + high) // 2 

            value = mid*mid

            if round(value) == x:
                return mid
            
            if round(value) > x:
                high = mid - 1
            
            else:
                if value > current:
                    current = mid
                    low = mid + 1
                else:    
                    low = mid + 1

        return high
            
