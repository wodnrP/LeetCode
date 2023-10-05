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