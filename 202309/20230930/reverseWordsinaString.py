class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(' ')
        r=''
        while s:
            if s[-1] != '':
                r=r+s.pop()+' '
            else:
                s.pop()
        r=r.strip()
        return r