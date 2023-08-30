class Solution:
    def twoSum(self, nums, target: int):
        for i, val in enumerate(nums):
                for j, val2 in enumerate(nums):
                    if i == j:
                        continue
                    if val + val2 == target:
                        return [i, j]
            
# 확인
"""
nums=[2,7,11,15]
target=9
print(Solution().twoSum(nums,target))
"""

# 수정 - 타임아웃
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#             l=0
#             r = 1
#             while l<len(nums)-1:
                
#                 if r > len(nums)-1:
#                     l+=1
#                     r = l+1

#                 if nums[l] + nums[r] == target:
#                     return [l, r]
                
#                 r+=1