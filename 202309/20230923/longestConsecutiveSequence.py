class Solution:
    def longestConsecutive(self, nums):
        """
        nums 리스트에서 중복제거
        sorted로 오름차순 정렬
        첫번째 리스트 값을 변수에 담기
        리스트 길이만큼 반복하는데
            변수 + 1이 리스트 값(2번 째)과 같으면
                카운트 + 1
            아니면
                카운트 결과 리스트에 추가
                카운트 = 0
            변수 = 리스트 값
        """
        if not nums:
            return 0
        nums = sorted(set(nums))
        n = nums[0]
        count = 0
        max_c = []
        for i in range(1,len(nums)):
            if n+1 == nums[i]:
                count+=1
            else:
                max_c.append(count+1)
                count=0
            n = nums[i]
        max_c.append(count+1)
        max_c.sort()
        return max_c[-1]