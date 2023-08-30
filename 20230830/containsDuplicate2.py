class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        """
        이해: 서로 다른 두 인덱스에 해당하는 값이 k번째 떨어져 있으면 True 아니면 False

        """ 
        hash_nums = {}
        # unduple = set(nums)
        # for i in nums:
        #     hash_nums = {i: []}
        # print(hash_nums)
        set_nums = set(nums)
        for j in set_nums:
            hash_nums[j]=None

        for i, val in enumerate(nums):
            if hash_nums.get(val) != None:
                hash_nums[val].append(i)
            
            else:
                hash_nums.update({val:[i]})

        for n in hash_nums:
            value = hash_nums.get(n)
            
            if len(value) >= 2:
                for l in range(len(value)):
                    if abs(value[l] - value[l+1]) == k:
                        return True
                    else:
                        return False
#확인
"""
nums = [1,2,3,1]
k = 3
print(Solution().containsNearbyDuplicate(nums, k))
"""