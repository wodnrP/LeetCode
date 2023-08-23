class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # nums1을 m번째 까지 슬라이싱하여 새로운 리스트1에 추가
        # nums2를 n번째 까지 슬라이싱하여 새로운 리스트1에 추가
        # for 만약 리스트1 0 > 리스트 1이면 자리 바꾸기
        del(nums1[m:])
        nums1[0:m] += nums2[0:n]

        # 1차
        # for i in range(1, m+n):
        #     for j in range(m+n):
        #         if nums1[i] < nums1[j]:
        #             nums1[i], nums1[j] = nums1[j], nums1[i]
        
        # 2차 수정 후
        nums1.sort()


# 확인
"""
nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
m=3
n=3
print(Solution().merge(nums1, m, nums2, n))
"""