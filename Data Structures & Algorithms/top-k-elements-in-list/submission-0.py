class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_map = {}

        for i, num in enumerate(nums):

            if num in nums_map:
                nums_map[num] += 1
            
            else: 
                nums_map[num] = 1
        
        sorted_nums_map = sorted(nums_map, key=nums_map.get, reverse=True)
        print(sorted_nums_map)

        return sorted_nums_map[:k]


        # Need to sort the dictionary so that most frequent is leftmost onwards
        # approach: get the values and append the key associated with it to the temp

        
        

'''
nums = ineger array
k = integer
    - k is most frequent elemnts within the array

The problem: test cases are generated such that the answer is always unique

return output does not need to be sorted
    
THE TASK: Given the length k, return the most frequent elements seen in the array (starting from most - least). The order of the output does not matter as long as [most-least] is adhered to before.

Approach 1: use hash map to count the frequencies, which then we get the top counts using the keys
    time > space
'''

