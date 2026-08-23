class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # initialise k
        # appraoch to use: single scan pair comparison

        k = 1
        n = 0 

        '''1 1 2 3 4 '''
        while n <= len(nums)-1:
        
            if nums[n] != nums[k-1]:
                nums[k] = nums[n]
                k +=1

            n+=1
        return k

'''
k will track both the location of the overwrite duplicate element and the count of the distinct element
n will scan the whole array (that's all it will do)

place x == place y:
    - k must not be += 1 since its a duplicate
    - we need to declare location k to be the place to overwrite the duplicate

if place x != place y:
    - k should stay in the same spot as before
    - overwrite place k with place x
    - record = place y
'''