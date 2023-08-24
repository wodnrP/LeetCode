class Solution(object):
    def canJump(self, nums):
        best=len(nums)-1
        for i in range(best,-1,-1):
            if best-i <= nums[i]:
                best = i
        if best == 0:
            return True
        else:
            return False
            

# 확인
"""
nums=[2,3,1,1,4]
print(Solution().canJump(nums))
"""