# 1번 
# class Solution(object):
#     def removeElement(self, nums, val):
#         i=0
#         while True:
#             if i >= len(nums):
#                 break

#             if nums[i] == val:
#                 del(nums[i])
#                 i -= 1
            
#             i+=1

#         return len(nums)


# 수정 후
class Solution(object):
    def removeElement(self, nums, val):
        i=0
        while True:
            if i >= len(nums):
                break

            if nums[i] == val:
                nums.remove(nums[i])
                i-=1
            
            i+=1

        return nums


# 확인
"""
nums=[0,1,2,2,3,0,4,2]
val=2
print(Solution().removeElement(nums, val))
"""