class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()

        def sum_check(indexvalue, equation):
            j, k = indexvalue+1, len(nums)-1

            while j < k:

                if nums[j] + nums[k] < -(equation):
                    j += 1
                elif nums[j] + nums[k] > -(equation):
                    k -= 1
                else:
                    result.append([nums[j], nums[k], nums[indexvalue]])   
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1 
        

        for i in range(len(nums)-1):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            sum_check(i, nums[i])


        return result