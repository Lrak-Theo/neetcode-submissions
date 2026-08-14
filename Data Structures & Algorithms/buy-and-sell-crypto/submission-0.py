class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1

        current_max_profit = 0

        if len(prices) <= 1:
            return current_max_profit

        while l < r:
            buy_price = prices[l]
            sell_price = prices[r]

            print(sell_price - buy_price)
            if sell_price - buy_price >= current_max_profit:
                current_max_profit = sell_price - buy_price
                r += 1
            else:
                r += 1        


            if r > (len(prices)-1):
                l += 1

                if l == (len(prices)-1):
                    return current_max_profit

                r = l + 1
            
    
            


'''
dyanmic sliding window question

have a counter of maximum profit currently achievable

iterate through the whole list

start from 0 - 1
if 0-1 > 0-2:
    then increase right pointer to right
if 0-1 < 0-2:
    then rewrite max profit to be 0-2


if there comes a time where for example the max length array read < max profit counter:
    then increase left pointer to right

if 1 - end > max profit:
    rewrite the max profit to be 1 - end
if 1 - 2nd < max profit:
    continue and so forth

'''