class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # 10,1,5,6,1,7
        
        # maxProfit = 6
        # left and right ptrs for window:
        # 1 7.
        # profit = right - left. if profit > max -> store.
        # if left >= right: left = right, right+=1 (to get smaller)
        # else: right += 1
        
        # return maxprofit IF it is > 0. else return 0.

        maxProfit = 0
        left = 0
        right = 1

        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit > maxProfit:
                maxProfit = profit
            if prices[left] >= prices[right]:
                left = right
            right += 1

        if maxProfit > 0:
            return maxProfit
        else:
            return 0
            