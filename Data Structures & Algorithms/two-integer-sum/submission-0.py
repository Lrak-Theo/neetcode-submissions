class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indices = {}

        for i, num in enumerate(nums):

            seen = target - num

            if seen in indices:
                return [indices[seen], i]
        
            indices[num] = i
            
        
        
        