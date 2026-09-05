class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        s = [letter for letter in s]
        l, r = 0, 0
        
        if not s:
            return 0

        # The dictionary will be act as the dynamic window
        hashmap = {}
        current_length = 0
        max_length = 0

        while r <= len(s)-1:

            if s[r] in hashmap:
                hashmap.pop(s[l])
                l += 1
        
            else:
                hashmap[s[r]] = r
                r += 1
                max_length = max(max_length, (r-l))    

        return max_length
