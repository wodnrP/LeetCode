class LinearProbingHash():

    def __init__(self, tableSize):
        self.tableSize = tableSize
        self.hashTable = {}
        for i in range(tableSize):
            self.hashTable[i] = {}


    # 해시 key 생성
    def get_hash_key(self, key):
        hashKey = hash(key) % self.tableSize
        return hashKey
    
    
    # hash key에 해당하는 주소에 key : value 쌍 저장
    def add_hash(self, key, value):
        hashKey = self.get_hash_key(key)
        if not self.hashTable[hashKey]:
            self.hashTable[hashKey][key] = value
            print(
                "hashKey 주소: ", hashKey, 
                "위치에 key:", key, 
                ",Value:", value, "이 저장 되었습니다."
                )
        else:
            _next = (hashKey + 1) % self.tableSize
            while self.hashTable[_next]:
                _next = (_next + 1) % self.tableSize
                if _next == hashKey:
                    print("빈 테이블이 없습니다.")
                    return print("**********저장 불가**********\n")
            self.hashTable[_next][key] = value
            print(
                "hashKey 주소: ", _next, 
                "위치에 key:", key, 
                ",Value:", value, "이 저장 되었습니다."
                )
    

    # value 불러오기
    def get_value(self, key):
        hashKey = hash(key) % self.tableSize
        check_key = hashKey
        while self.hashTable[hashKey] and key not in self.hashTable[hashKey]:
            hashKey = (hashKey+1) % self.tableSize
            if hashKey == check_key:
                return None
        return self.hashTable[hashKey][key]
        

# 동작 확인
testHashTable = LinearProbingHash(5)
testHashTable.add_hash("continued",10)
testHashTable.add_hash("success",20)
testHashTable.add_hash("unnoticed",30)

print("key 값 continued의 value는 ",testHashTable.get_value('continued'))
print("key 값 success의 value는 ",testHashTable.get_value('success'))
print("key 값 unnoticed의 value는 ",testHashTable.get_value('unnoticed'))
        

