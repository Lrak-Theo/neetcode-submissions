class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:


        for x in range(len(nums)):
            if nums[x] == target:
                return x

            if nums[x] > target:
                return nums.index(nums[x])
  
        return x + 1
            
    

       

    


'''
array always has distinct integers
target value

return index (location in list) if target is found

return the index where it ould be if it were inserted in order

O(log n) target
'''