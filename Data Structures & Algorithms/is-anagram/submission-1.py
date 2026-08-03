class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hash_map_s = {}

        for letter in list(s.lower()):

            if letter in hash_map_s:
                hash_map_s[letter] += 1

            else:
                hash_map_s[letter] = 1

        hash_map_t = {} 

        for letter in list(t.lower()):

            if letter in hash_map_t:
                hash_map_t[letter] += 1

            else:
                hash_map_t[letter] = 1


        if hash_map_s == hash_map_t:
            return True
        else:
            return False