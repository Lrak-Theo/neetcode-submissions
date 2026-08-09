class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        
        for x in nums:
            
            if x in freq:
                freq[x] += 1
            
            else:
                freq[x] = 1

        return max(freq, key=freq.get)

'''
goal: return the element that appears the most in the array

statement: majority == appearing more than n/2 times
'''