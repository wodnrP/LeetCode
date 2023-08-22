class Solution(object):
    def removeDuplicates(self, nums):
        i = 1
        while True:
            if i >= len(nums):
                break

            if nums[i-1] == nums[i]:
                del(nums[i])
                i-=1
            
            i += 1
        
        return nums

"""
# 확인
nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))
"""