# 1차
# class Solution:
#     def findMin(self, nums):
#         n = sorted(nums) 
#         return n[0]

# 수정 후
class Solution:
    def findMin(self, nums):
        l,r = 0,len(nums)-1

        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]
            
            avg = (l + r) // 2

            if nums[l] > nums[avg]:
                r = avg
            else:
                l = avg + 1