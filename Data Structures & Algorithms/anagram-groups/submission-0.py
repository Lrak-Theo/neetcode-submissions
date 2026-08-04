class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap_word = {}

        for word in strs:

            key = ''.join(sorted(word))
            if key in hashmap_word:
                hashmap_word[key].append(word)
            else:
                hashmap_word[key] = [word]


        return list(hashmap_word.values())
                


                        
                        

                    

                