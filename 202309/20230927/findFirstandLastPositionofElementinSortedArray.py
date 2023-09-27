class Solution:
    def searchRange(self, nums, target):
        l,r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2 
            if nums[l] == nums[r] == target:
                return [l, r]
            if nums[mid] > target:
                r = mid - 1 
            if nums[mid] < target:
                l = mid + 1
            else:
                if nums[l] != target:
                    l += 1
                if nums[r] != target:
                    r -= 1
        return [-1, -1]