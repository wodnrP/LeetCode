class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        1. 만약 target in nums:
            return 1
        2. sumnums=[nums[0], nums[1]]
        3.  n=1
            while nums:
                만약 n > len(nums):
                    return 0

                만약 j == len(nums):
                    n+=1

                만약 sum(sumnums) < target:
                    sumnums.remove(nums[0])
                    for i in range(n):
                        sumnums.append(nums[i+j])
                
                만약 sum(sumnums) == target:
                    return len(sumnums)
        
        # 첫 시도 fail
        if target in nums:
            return 1
        sumnums=[nums[0], nums[1]]
        n = 1
        j = 1
        while nums:
            if j == len(nums)-1:
                n+=1
                j=0
            if n == len(nums) or sum(nums)<target:
                return 0
            
            if sum(sumnums) < target:
                sumnums.remove(sumnums[0])
                for i in range(n):
                    sumnums.append(nums[i+j+1]) 

            if sum(sumnums) == target:
                return len(sumnums)
            j+=1
        """

        """
        만약 target이 nums에 포함 되면 return 1
        
        nums를 내림차순으로 정렬 
        l과 r 포인터
        
        total=nums[l]+nums[r]
        
        만약 total >= target:
            return 2
        
        elif total < target:
            for i in range(w):
                total+=nums[r+i]    
            
            
            

        """
        if target in nums:
            return 1
        
        nums = sorted(nums, reverse=True)
        print(nums)
        total = nums[0]+nums[1]
        for i in range(2,len(nums)):
            if total >= target:
                return i+1
            total+=nums[i]
            print('nums[',i,']=', nums[i], 'total=',)
# 확인
nums=[12,28,83,4,25,26,25,2,25,25,25,12]
# 83 28 26 25 25 25 25 25 12 12 4 2
target=213
print(Solution().minSubArrayLen(target, nums))