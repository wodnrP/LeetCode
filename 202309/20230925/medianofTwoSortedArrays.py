class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums=sorted(nums1+nums2)
        mid=len(nums)//2
        if len(nums)%2!=0:
            return nums[mid]
        else:
            return (nums[mid] + nums[mid-1])/2