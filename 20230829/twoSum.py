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