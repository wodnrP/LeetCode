# class Solution(object):
#     def rotate(self, nums, k):
#         for i in range(k):
#             nums.insert(0, nums.pop())

# class Solution(object):
#     def rotate(self, nums, k):
#         # testcase 중 k가 0일 경우 과정거치지 않고 그대로 반환
#         if k==0:
#             return nums

#         for i in range(k%len(nums)):
#             # nums 마지막 요소 저장
#             pop = nums[-1]
#             # 마지막 요소 삭제
#             del nums[-1]
#             # 첫번째에 추가 
#             nums.insert(0, pop)

#         return nums

class Solution(object):
    def rotate(self, nums, k):
        count = len(nums)
        # testcase 중 k가 0일 경우 과정거치지 않고 그대로 반환
        if k==0 or count<=1:
            return nums

        if count < k:
            nums[:] = nums[count-(k%count):] + nums[:-(k%count)]
            return nums

        # nums[-k]번째까지 슬라이싱 + nums 개수 k로 나눈 나머지 값까지 슬라이싱
        nums[:] = nums[-k:] + nums[:-(k%count)]
        
        return nums

"""
#확인
nums = [-1]
k=2
print(Solution().rotate(nums, k))
"""