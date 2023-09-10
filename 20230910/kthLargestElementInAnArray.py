class Solution:

    def findKthLargest(self, nums, k):

        # 하위트리 반복 bubledown 정렬
        self.bubledown(nums, len(nums), 0)
        
        # 리프 노드 인접 값 정렬 
        self.childsort(nums)
        return nums[k-1]

    def bubledown(self, nums, n, i):
        small = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and nums[i] > nums[left]:
            small = left

        if right < n and nums[small] > nums[right]:
            small = right

        if small != i:
            nums[i], nums[small] = nums[small], nums[i]
            self.bubledown(nums, n, small)


    def childsort(self, nums):
        n = len(nums)

        for i in range(n//2 - 1 , -1 , -1):
            self.bubledown(nums, n, i)
        
        for i in range(n-1 ,0 ,-1):
            nums[i],nums[0]=nums[0],nums[i]
            self.bubledown(nums, i, 0)