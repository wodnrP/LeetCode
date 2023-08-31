class Solution:
    def isHappy(self, n: int) -> bool:
        k = str(n)
        r = 0
        
        while k != '1':
            if k == '1' or k =='7':
                return True
            
            elif int(k) < 10:
                return False

            for i in range(len(k)):
                r += int(k[i])**2
            
            k = str(r)
            r = 0

            continue
        return True