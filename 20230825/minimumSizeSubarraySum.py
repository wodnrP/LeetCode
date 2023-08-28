# 실패한 시도 - 연속된 하위 배열 시퀀스가 아님 
# class Solution(object):
#     def minSubArrayLen(self, target, nums):
#         if target in nums:
#             return 1
#         if sum(nums) < target:
#             return 0
#         if sum(nums) == target:
#             return len(nums)
        
#         total = 0
#         for i in range(len(nums)):
#             total+=nums[i]

#             if total >= target:
#                 return i

# time over
class Solution(object):
    def minSubArrayLen(self, target, nums):
        for i in range(len(nums)):
            if target <= nums[i]:
                return 1
        if sum(nums) < target:
            return 0
        if sum(nums) == target:
            return len(nums)


        n = [nums[0]]
        i=1
        next=1
        save=[]
        while next-1 < len(nums)-1:

            if i > len(nums)-1:
                del n[:]
                i = next
                next+=1
            
            n.append(nums[i])
            
            if sum(n) >= target:
                save.append(len(n))
            i+=1
        
        return min(save)


# 확인 - 해당 테스트 케이스 오류 (연속된 배열 시퀀스에서 최소 합)
nums=[12,28,83,4,25,26,25,2,25,25,25,12]
# 83 28 26 25 25 25 25 25 12 12 4 2
target=213
print(Solution().minSubArrayLen(target, nums))