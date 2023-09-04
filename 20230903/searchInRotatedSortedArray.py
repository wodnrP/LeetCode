class Solution:
    def search(self, nums, target):
        """
        sort()로 정렬 후 - O(nlogn)
        이진 검색
        """
        sort_nums = sorted(nums)
        l,r = 0,len(nums)-1
        
        if r == 0 and nums[0] == target:
            return 0

        while l <= r:
            avg = (l+r)//2
            if sort_nums[avg] == target:
                return nums.index(target)
            if sort_nums[avg] < target:
                l = avg + 1
            else:
                r = avg - 1

        return -1