# 1차 시도
# class Solution(object):
#     def maxProfit(self, prices):
#         # 리스트 내 최소값 이후 값 중 가장 큰 값의 차이 구하는 것 
#         buy=min(prices)

#         if len(prices[prices.index(buy)+1:])==0:
#             return 0
        
#         sell=max(prices[prices.index(buy)+1:])

#         return sell-buy

# 2차 시도 
# class Solution(object):
#     def maxProfit(self, prices):
#         # 구매한 날짜로 부터 오른쪽으로 탐색했을 때 그 격차가 가장 큰 값 반환
#         # 첫번째 구매시 큰값 
#         # 두번째 구매시 큰값
#         j=1
#       sell=0

#       for i in range(len(prices)):
#           if j >= len(prices):
#               break

#           if prices[j-1] - prices[j] < 0:
#               for k in range(j,len(prices)):
#                   if sell > prices[j-1] - prices[k]:
#                       sell=prices[j-1] - prices[k]
#           j+=1
        
#       return abs(sell)

# 1차
# class Solution(object):
#     def maxProfit(self, prices):
#         if len(prices)==0:
#             return 0
        
#         buy=prices[0]
#         sell=0

#         for i in range(1,len(prices)):
#             buy=min(buy, prices[i])
#             sell=max(sell, prices[i]-buy)

#         return sell

# 수정 후
class Solution(object):
    def maxProfit(self, prices):
        if len(prices)==0:
            return 0
        buy=prices[0]
        sell=0
        for i in range(1,len(prices)):
            if buy > prices[i]:
                buy=prices[i]
            if sell<(prices[i]-buy):
                sell=prices[i]-buy 
        return sell

# 확인 
"""
prices=[7,1,5,3,6,4]
print(Solution().maxProfit(prices))
"""