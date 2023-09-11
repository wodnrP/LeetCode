class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        import heapq

        heap = []
        result = []
        nums = nums1 + nums2
        
        for i in nums:
            if len(nums) == k:
                result = nums
                break

            heapq.heappush(heap, i)
            if len(heap) > k-1:
                result.append(heapq.heappop(heap))

        result = [[result[0], r] for r in result[1:]]
        return result[:k]
    
"""
nums1 = [1,2], nums2 = [3] 
ouput = [[1,2],[1,3]]
expected = [[1,3],[2,3]]
"""