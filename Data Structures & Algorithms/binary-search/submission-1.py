class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start, end = 0, len(nums) - 1

        while start <= end:
            m = (start + end) // 2

            if nums[m] > target:
                end = m - 1
            
            elif nums[m] < target:
                start = m + 1 
            else:
                return m
            
        return -1
            
 
        ''' 
        nums is in ascending order and all values are distinct
        target is integer

        search for target within num

        divide and conquer algo
            - search middle
                - if middle == target return the middle
                - if not compare left and right if its the target
                    - since its sorted if middle >= target we search left else search right
                    - eventually finding the target
        '''