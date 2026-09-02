class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # nums1 and nums2 is sorted

        # merge both arrays such that they are sorted as well as all in nums1 
        
        # nums1 will have 0 values acting as placeholders for the values for nums2

        # each time an nums2[element] is in the correct element spot in nums1 to insert, the rest   should be pushed right

        i = m-1
        j = len(nums2)-1
        k = m+n-1
    
        while i >= 0 and j >= 0:
            # elements after m is 0s, as 0s get filled decrement track, need to decrement fast
            # If element j is bigger than element i, put j in the k position and decrement
            if nums2[j] >= nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            
            # If element j is smaller than element i, put i into k position and decrement
            else:
                nums1[k] = nums1[i]
                i -= 1 
            
            k -= 1
        
        # If j still remains to be filled, then fill it at the start array
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1 
            
