class Solution:
    def canConstruct(self, ransomNote, magazine) -> bool:
        """
        magazine 문자열로 ransomNote를 만들 수 있으면 true 아니면 false
        단, magazine 문자열은 중복 사용 불가

        ransomNote의 중복값을 배제한 리스트의 값으로 key 생성

        ransomNote 값이 key로 담긴 딕셔너리의 value에 값들의 개수 저장

        magazine도 같은 방법으로 딕셔너리 생성 

        ransomNote 키에 해당하는 value 보다 동일한 key를 가지고 있는 magazin의 value가 없거나 작으면 false
        
        아니면 true
        """
        ran = set(ransomNote)
        mag = set(magazine)

        ran_dict = {}
        mag_dict = {}

        for i in ran:
            ran_dict[i] = ransomNote.count(i)
        
        for j in mag:
            mag_dict[j] = magazine.count(j)
    
        for r in ran_dict:
            if mag_dict.get(r) == None:
                return False
            if ran_dict.get(r) > mag_dict.get(r):
                return False
        return True