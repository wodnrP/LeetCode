import random
class RandomizedSet:
    def __init__(self):
        self.ran_set=[]
        self.ran_hash={}
    
    def insert(self, val: int) -> bool:
        if val in self.ran_hash.keys():
            return False
        else:
            self.ran_hash[val]=None
            self.ran_set.append(val)
            return True
    
    def remove(self, val: int) -> bool:
        try:
            del self.ran_hash[val]
            self.ran_set.remove(val)
            return True
        except KeyError:
            return False
    
    def getRandom(self) -> int:
        return random.choice(self.ran_set)