class Solution(object):
    def twoSum(self, numbers, target):
        """
        1. left, right 포인터 활용
        2. numbers[l] + numbers[r] > target이면, 
            right 포인터 감소
        3. numbers[l] + numbers[r] < target이면,
            left 포인터 증가

        4.  numbers[l] + numbers[r] == target
            result.append(l+1)
            result.append(r+1)

        5. result 반환
        """
        i=0
        l,r=0,len(numbers)-1
        result=[]
        while numbers:
            if l >= r:
                break

            if numbers[l] + numbers[r] > target:
                r-=1

            elif numbers[l] + numbers[r] < target:
                l+=1

            else:
                result.append(l+1)
                result.append(r+1)
                break
            
            i+=1
        return result
#확인
"""
numbers=[2,7,11,15]
target=9
print(Solution().twoSum(numbers, target))
"""