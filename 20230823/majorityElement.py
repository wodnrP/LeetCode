# 1차
# class Solution(object):
    
#     def majorityElement(self, nums):
#         count=[]
#         num=set(nums)
#         for i in num:
#             count.append(nums.count(i))
        
#         result=list(num)
#         return result[count.index(max(count))]

# 2차
class Solution(object):
    
    def majorityElement(self, nums):
        major = 0
        num=list(set(nums))
        count=0

        for i in range(len(num)):
            if nums.count(num[i]) > count:
                count = nums.count(num[i])
                major = num[i]
        return major


# 확인
"""
nums = [3,2,3]
print(Solution().majorityElement(nums))
"""