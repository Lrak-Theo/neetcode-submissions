# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        ''' my guess should fall within the range of 1-n'''

        low = 0
        high = n

        while low <= high:
            mid_point = low + (high - low) // 2

            if guess(mid_point) == 0:
                return mid_point

            elif guess(mid_point) == -1: #higher than the number the system picked
                high = mid_point - 1
            
            else: #lower than the number the system picked
                low = mid_point + 1
