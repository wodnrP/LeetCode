class Solution:
    def maxArea(self, height):
        """
        포인터 2개로 
        처음과 끝이 가르키는 포인터 중 작은 값 x 오른쪽 포인터 - 왼쪽 포인터 + 1
        max = 0 이라는 변수에 최대값을 갱신
        작은 값을 가진쪽을 += 1 이동 
        만약 오른쪽 포인터와 왼쪽이 같으면 break
        """
        l,r = 0,len(height)-1
        amount = 0

        while l != r:
            x = min(height[l], height[r])
            amount = max(amount, (x * (r-l)))
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1
        return amount