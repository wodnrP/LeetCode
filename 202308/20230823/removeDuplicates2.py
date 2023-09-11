# class Solution(object):
#     def removeDuplicates(self, nums):
#         k=len(nums)
#         j=2
#         for i in range(2, k):

#             if nums[j] == nums[j-1] == nums[j-2]:
#                 print(j, nums, k)
#                 del(nums[j-2])
#                 k=k-1
#                 j-=1
#             j+=1
                
#         return nums

# 수정 1차
class Solution(object):
    def removeDuplicates(self, nums):
        j=2
        for i in range(2, len(nums)):
            if nums[i] != nums[j-2]:
                nums[j] = nums[i]
                j+=1    
        return j

# 수정 2차
# class Solution(object):
#     def removeDuplicates(self, nums):
#         j=2
#         for i in range(2, len(nums)):
#             if nums[i] == nums[j-2]:
#                 continue
#             nums[j] = nums[i]
#             j+=1
                
#         return nums

#확인
"""
nums = [0,0,0,0,0]
print(Solution().removeDuplicates(nums))
"""
# i = 2, 3, 4, 5, 6, 7, 8, 9
# i = 2
# nums[2] == [1] == [0] -> x
# i = 3
# nums[3] == [2] == [1] -> x
# i = 4
# nums[4] == [3] == [2] -> o
# nums[2] x ->  nums[0,0,1,1,1,2,3,3]
# k = 8
# i = 3
# -> x
# i = 4
# nums[4] == [3] == [2] -> o
# nums[2] x -> nums[0,0,1,1,2,3,3] 