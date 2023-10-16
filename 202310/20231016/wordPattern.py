class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split(' ')
        w_dict = {}
        if len(pattern) != len(word):
            return False
        for i, d in enumerate(pattern):
            if d in w_dict and w_dict[d] != word[i]:
                return False
            elif d not in w_dict and word[i] in w_dict.values():
                return False
            elif d not in w_dict:
                w_dict[d] = word[i]
        return True 
