class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        문자열 만큼 반복하는데,
        윈도우 생성 = 1
        문자 길이 만큼 반복
            만약 윈도우 범위에 해당하는 문자가 아니면 
                윈도우 += 1
            만약 윈도우 범위에 해당하는 맞으면
                윈도우 = 1

        # 방법 2
        윈도우 범위 생성 = 1
        윈도우 리스트 = 문자열[0]
        
        만약 문자열[1]이 윈도우 리스트에 없으면
            윈도우 범위 += 1
            문자열[1]을 윈도우 리스트에 추가
        
        만약 문자열[1]이 윈도우 리스트에 있으면
            문자열[0]삭제
        """
        window = [s[0]]

        w = 1
        while w+1 <= len(s):
            if s[w] not in window:
                window.append(s[w])
            else:
                pass
            w+=1 
        return len(window)
    
# 확인

s="abcabcbb"

print(Solution().lengthOfLongestSubstring(s))