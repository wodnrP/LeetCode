class Solution(object):
    def searchInsert(self, nums, target):
        """
        만약 target이 배열 내에 없으면 len(nums) 반환

        왼쪽, 오른쪽 포인터 생성 
        nums만큼 반복하는데

        왼쪽 오른쪽 값이 같으면 break

        만약 왼쪽 + 오른쪽 평균 > target이면
        왼쪽 포인터 값에 왼쪽 오른쪽 평균 +

        만약 왼쪽 + 오른쪽 평균 < target이면
        오른쪽 포인터 값에 왼,오 평균 -

        num[아무 포인터 값] 리턴 
        """
        left, right = 0, len(nums)-1

        while left <= right:
            avg = (left+right)//2
            
            if nums[avg] == target:
                return avg

            if nums[avg] < target:
                left = (avg+1)

            else:
                right = (avg-1)

        return left
# nums[avg]를 해야하는데 avg와 target값만 비교해서 오류가 발생한 것임 

# 확인
"""
nums=[1,3,5,6]
target=2
print(Solution().searchInsert(nums, target))
"""