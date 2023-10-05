class Solution:
    def singleNumber(self, nums) -> int:
        nums = sorted(nums)
        i,j=0,1
        while len(nums) > j:
            if nums[i] != nums[j]:
                return nums[i]
            i+=2
            j=i+1
        return nums[i]

# 솔루션 코드 추가 : 비트연산 
# class Solution:
#     def singleNumber(self, nums) -> int:
#         num = 0
#         for i in nums:
#             num ^= i
#         return num