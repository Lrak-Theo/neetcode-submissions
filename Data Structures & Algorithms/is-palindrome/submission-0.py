import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        '''
        goal is to find if s is a palindrome

        s needs to be duplicated but in reverse

        where s_reversed = s.reverse()??'''

        s = re.sub(r'[^a-zA-Z0-9]', '', s).strip(" ").lower()
        s_reversed = s[::-1]


        if s == s_reversed: 
            return True
        
        else:
            return False



