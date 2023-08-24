class Solution(object):
    def maxProfit(self, prices):
        if len(prices)==0:
            return 0
        
        k = len(prices)
        sell=[]
        for i in range(k):
            # prices[i+1]의 index out of range 방지
            if i+1 == k:
                break

            if prices[i] < prices[i+1]:
                # print('prices[',i,']=',prices[i],'prices[',i+1,']=',prices[i+1])
                sell.append(prices[i+1] - prices[i])

        return sum(sell)

# 수정 후
# class Solution(object):
#     def maxProfit(self, prices):
#         if len(prices)==0:
#             return 0
#         k = len(prices)
#         sell=0
#         for i in range(k-1):
#             if prices[i] < prices[i+1]:
#                 sell+=prices[i+1]-prices[i]
#         return sell
# i=0 / 7 < 1 
# i=1 / 1 < 5 5-1 = 4
# i=2 / 5 < 3
# i=3 / 3 < 6 = 6-3 3 
# i=4 / 6 < 4 
#4+3 = 0

#확인
"""
prices=[7,6,4,3,1]
print(Solution().maxProfit(prices))
"""