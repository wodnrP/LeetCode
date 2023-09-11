# in 연산자로 각 행마다 target값 있는지 확인 - 초기 접근 법
# class Solution(object):
#     def searchMatrix(self, matrix, target):
#         for i in range(len(matrix)):
#             if target in matrix[i]:
#                 return True
#         return False

class Solution(object):
    def searchMatrix(self, matrix, target):
        # 각 행의 마지막 값 보다 다음 행이 크다 = 오름차순 정렬된 리스트
        # 정렬된 리스트의 이진 검색
        
        # 왼쪽 포인터, 오른쪽 포인터 ((각 행 속 요소 개수 x 행의 개수) -1)
        matrix=sum(matrix,[])

        l,r=0, len(matrix)-1
        while l <= r:
            avg = (l+r)//2
            if matrix[avg] == target:
                return True
            if matrix[avg] < target:
                l = avg + 1
            else:
                r = avg - 1

        return False
        
        
#확인
"""
matrix=[[1,1]]
target=2

print(Solution().searchMatrix(matrix, target))
"""