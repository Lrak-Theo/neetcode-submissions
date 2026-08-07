class KthLargest:

    def __init__(self, k: int, nums: List[int]):
            self.k = k
            self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        
        nums_sorted = sorted(self.nums)

        return nums_sorted[-self.k]
            
'''

what does add(val) need to do:
1. add the integer val into the stream / array not necessarily needing to sort it.
    - meaning it is added last in the priority queue ([-1] index value)
2. find kth leagest integer in this function
    - compare 


nums = is a list of elements paired with a queue (starting from 0)
k = is the kth largest integer to find
Values can have duplicates

e.g. 3rd largest
1 2 3 3 3 5 6 7

max(num) = 7

better way, sort it
then get the 3rd largest by index

return max(num) 
'''
