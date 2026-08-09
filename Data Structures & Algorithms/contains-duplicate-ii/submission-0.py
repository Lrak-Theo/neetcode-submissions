class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set() # Initialised a set

        l = 0 # Create our left pointer

        for r in range(len(nums)): # r in this case will be our right pointer that iterates constantly

            if r - l > k: # We use the l value to find if our current index difference meets the condition of less than k
                window.remove(nums[l]) # if it does not and is over, we need to remove l element (the leftmost)
                l += 1 # we count up indicating we moved to the next element as the check
            
            if nums[r] in window: # if the element is seen in the window set we can now return True
                return True

            window.add(nums[r]) # else we add the element, iterating unitl the end or false
        
        return False
        
            