# 1차
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         # t 안에 s가 있는지 확인
#         # for i in s:
#         #     if i not in t:
#         #         return False
#         # return True 

#         # t 안에 s가 있는지 확인
#         # 단, a가 있는지 확인 되면 a 위치까지 슬라이싱 
#         for i in s:
#             if i not in t:
#                 return False
#             if i in t:
#                 t = t[t.index(i)+1:]
#         return True

# 수정 후
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer = 0
        if len(s) == 0:
            return True

        for i in t:
            if len(s) <= pointer:
                break
            if s[pointer] == i:
                pointer += 1
        
        if len(s) == pointer:
            return True
        else:
            return False