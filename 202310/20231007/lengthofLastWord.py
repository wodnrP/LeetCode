# 첫번째 방법
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         s=s.rstrip().split(' ')
#         return len(s[-1])
    
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        i=1
        while len(s)>i:
            if s[-i] == ' ':
                return i-1
            i+=1  
        return i