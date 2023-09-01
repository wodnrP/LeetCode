class LinearProbingHash():

    def __init__(self, tableSize):
        self.tableSize = tableSize
        self.hashTable = [{} for _ in range(tableSize)]

    # 해시 key 생성
    def get_hash_key(self, key):
        hashKey = 0

        for i in key:
            hashKey += ord(i) + ord('a')

        hashKey %= self.tableSize
        return hashKey
    
    # key가 있는지 확인
    def key_check(self, hashTable, key):
            for i, table in enumerate(hashTable):
                if key in table:
                    return True
            return False
    
    # hash key에 해당하는 주소에 key : value 쌍 저장
    def add_hash(self, key, value):
        hashKey = self.get_hash_key(key)

        if not self.hashTable[hashKey]:
            self.hashTable[hashKey] = {key : value}
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

            self.hashTable[_next] = {key : value}
            print(
                "hashKey 주소: ", _next, 
                "위치에 key:", key, 
                ",Value:", value, "이 저장 되었습니다."
                )
    
    # value 불러오기
    def get_value(self, key):
        hashKey = self.get_hash_key(key)

        if self.key_check(self.hashTable, key):
            for i in self.hashTable:
                if key in i:
                    # i.values = dict([값])이 나와서 
                    # print문 깔끔히 하기 위해 임의 사용
                    return next(iter(i.values()))
        
        else:
            _next = (hashKey + 1) % self.tableSize

            while not self.key_check(self.hashTable, key):
                _next = (_next+1) % self.tableSize

                if _next == hashKey: 
                    print("해당 key",key,"의 값을 찾지 못했습니다.")
                    return "없습니다."
            
            return self.hashTable[_next]
        

# 동작 확인
testHashTable = LinearProbingHash(2)
testHashTable.add_hash("continued",10)
testHashTable.add_hash("success",20)
testHashTable.add_hash("unnoticed",30)

print("key 값 continued의 value는 ",testHashTable.get_value('continued'))
print("key 값 success의 value는 ",testHashTable.get_value('success'))
print("key 값 unnoticed의 value는 ",testHashTable.get_value('unnoticed'))
        

