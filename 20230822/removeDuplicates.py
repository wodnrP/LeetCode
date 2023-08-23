# 1차
# class Solution(object):
#     def removeDuplicates(self, nums):
#         i = 1
#         while True:
#             if i >= len(nums):
#                 break

#             if nums[i-1] == nums[i]:
#                 del(nums[i])
#                 i-=1
            
#             i += 1
        
#         return nums

# 1차 수정 후
# class Solution(object):
#     def removeDuplicates(self, nums):
#         nums[:] = sorted(set(nums))
#         return nums
    
# 2차 수정 후
class Solution(object):
    def removeDuplicates(self, nums):
        i = 1
        j = 1
        while True:
            if i >= len(nums):
                break

            if nums[i-1] != nums[i]:
                nums[j] = nums[i]
                j+=1
            
            i+=1
        
        return j
# 확인
"""
nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))
"""
