import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # question sounds similar to koko banana
        # max is given -> sum(weights)

        # task: find the least weight capacity that ships within days given


        # we can look at evening the weights out
        # or we can go by day 

        def find_min(weights, days, var):
            weight_acc = 0
            day_acc = 0

            if var < max(weights):
                return False
            
            for i in weights:
                if weight_acc + i > var:
                    day_acc += 1
                    weight_acc = 0
                weight_acc += i

            if weight_acc > 0:
                day_acc += 1 
                
            if day_acc <= days:
                return var
            
            else:
                return False
        
        low = 1
        min_w = sum(weights)
        high = min_w

        while low <= high:
            mid = (high+low) // 2

            w = find_min(weights, days, mid)

            if w == False:
                low = mid + 1

            else: 
                min_w = min(min_w, w)
                high = mid - 1
                
            
        return min_w
                
      
            
