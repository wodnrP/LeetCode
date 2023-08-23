class Solution(object):
    
    def majorityElement(self, nums):
        count=[]
        num=set(nums)
        for i in num:
            count.append(nums.count(i))
        
        result=list(num)
        return result[count.index(max(count))]

"""
# 확인
nums = [3,2,3]
print(Solution().majorityElement(nums))
"""