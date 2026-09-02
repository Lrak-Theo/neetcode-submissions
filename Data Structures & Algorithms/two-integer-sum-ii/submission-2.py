class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # numbers is sorted in non-decreasing order == smallest values -> higher values no order
        # track the indicies (starting from 1), index1 index2
        # index1 + index2 needs to add up == target
            # index1 also needs to be less than index2
            # index1 != index2 // don't use the same element twice
        # Only 1 valid solution
        # return the indices tracked correctly
        # O(1) additional space == no new space needs to be initialised persistently

        # Two pointer (with target as a constant)
        l, r = 0, len(numbers)-1

        while True:

            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            
            if numbers[l] + numbers[r] > target:
                r -= 1
            
            else:
                l += 1

        '''
        # Brute force method first (O(n**2))
        for i in range(low, mid):

            for j in range(low, mid):

                if numbers[i] + numbers[j] == target and i != j:
                    return [i+1, j+1]
        '''


        ''' edge case testing:
            can not be be empty != []
            can have the same numbers, distinct is not stated
            negative elements are evident as well as negative targets
        '''

        ''' assumption for now:
            the target refers to the numbers[index1] + numbers[index2]
        '''