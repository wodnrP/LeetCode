# 1차
# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         1. 모두 소문자로 변환한다
#         2. a-z까지 해당 할 경우 새로운 변수에 문자할당
#         3. left, right 포인터 생성 
#         4. l과 r의 위치에 해당하는 문자열 비교 같으면 l=증가 r=감소
#         5. 틀리면 false
#         """
#         s=s.lower()
#         new=""
#         for i in s:
#             if i.isalnum():
#                 new+=i
        
#         r=len(new)-1
#         for l in range(len(new)):
#             if l >= r:
#                 break

#             if new[l] != new[r]:
#                 return False
            
#             r-=1
        
#         return True

# 2차 수정완료
class Solution(object):
    def isPalindrome(self, s):
        l,r=0,len(s)-1

        while l < r:
            if not s[l].isalnum():
                l+=1

            elif not s[r].isalnum():
                r-=1

            elif s[l].lower() != s[r].lower():
                return False
            
            else:
                l += 1
                r -= 1
        
        return True


# 확인
"""
s="A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))
"""