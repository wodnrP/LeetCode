# 1차
# class Solution:
#     def findPeakElement(self, nums):
#         """
#         sorted 함수 = 병합정렬기반 O(nlogn) 보장
#         주변 값들 중 가장 큰 값의 인덱스 == 가장 큰 값의 인덱스 
#         """
#         sort_check = sorted(nums)
#         return nums.index(sort_check[-1])

# 수정 후 
class Solution:
    def findPeakElement(self, nums):
        # nums 길이가 1 이거나 0번째가 첫번째 보다 큰 경우 0
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0

        # 마지막 요소가 그 전 요소보다 크면 마지막 인덱스 값 
        elif nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums) - 1

        l,r= 0, len(nums)-1
        while l <= r:
            avg = (l+r) // 2
            if nums[avg] > nums[avg+1] and nums[avg] > nums[avg-1]:
                return avg
            elif nums[avg] > nums[avg+1]:
                r = avg - 1
            else:
                l = avg + 1