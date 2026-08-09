class Solution:

    def merge_sort(self, array):
        if len(array) <= 1:
            return array

        array_a = array[:(len(array)//2)]
        array_b = array[(len(array)//2):]

        sorted_array_a = self.merge_sort(array_a)
        sorted_array_b = self.merge_sort(array_b)

        return self.merge_array(sorted_array_a, sorted_array_b)

    def merge_array(self, left, right):
        sorted_array = []
        i, j = 0, 0

        while i < len(left) and j < len(right): # Two finger 
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1

        # If the other lements are sorted
        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])

        return sorted_array

    def sortArray(self, nums: List[int]) -> List[int]:
        
        return self.merge_sort(nums)


'''
sort nums in ascending order, return the same array (assuming)
cant use any built in functions
time goal: O(n log(n))
    - n = an array scan 
    - log(n) = potentially don't need to sort the whole array (reason being some elements ARE already in ascending order)
space goal: smallest as possible 

first proposal: 2 pointer approach comapre first element against last element, swap when needed, then iterate until l > r
    - Sort name: Merge sort
    - edge case:
        - what if first element == last element?
        - what if the array is only one
        - what if the array is empty
'''