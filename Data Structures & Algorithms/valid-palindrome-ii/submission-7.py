class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def is_palindrome(sub_s):
            return sub_s == sub_s[::-1]

        s = list(s)

        l, r = 0, len(s) - 1

        while l < r:

            if s[l] != s[r]:
                
                if is_palindrome(s[l:r]) or is_palindrome(s[l+1:r+1]):
                    return True
                else:
                    return False
            
            l+=1
            r-=1
        return True


'''
we check for the odd one out 
left to right
so if l[0] == l[-1]:
    continue:

if its not equals to:
    we can remove that element in the string
    then continue / loop again using the same parameters


can only delete 0-1 character 
'''