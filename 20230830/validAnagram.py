class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = set(s)
        set_t = set(t)

        s_dict = {}
        t_dict = {}

        for i in set_s:
            s_dict[i] = s.count(i)
        
        for j in set_t:
            t_dict[j] = t.count(j)
        
        # 두 dict 중 key 값이 더 많은 dict 반환
        new_dict={}

        if len(s_dict) > len(t_dict):
            new_dict = s_dict
        else:
            new_dict = t_dict

        for r in new_dict:
            if s_dict.get(r) == None or t_dict.get(r) == None:
                return False
            if s_dict.get(r) > t_dict.get(r):
                return False
        return True