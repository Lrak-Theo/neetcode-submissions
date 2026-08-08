class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        x = 0
        same = 0
        while x < len(nums):
            if nums[x] != val:
                nums[same] = nums[x]
                same += 1
            x += 1
        
     
        return same

'''
need to remove val integers in nums if it exists (in-place)
order of elements may be changed

return number of element in nums which are not equal to val (defined as k)

extra:
    - change the array nums where the k elements contain the elements which are not equal to val
    - basically move the elements that are not val to in the beginning

3 2 2 3 val = 3  k = 2 

''' 