class LinearProbingHash():

    def __init__(self, tableSize):
        self.tableSize = tableSize
        self.hashTable = [{} for _ in range(tableSize)]

    # 해시 key 생성
    def get_hash_key(self, key):
        hashKey = 0

        for i in key:
            hashKey += ord(i) - ord('a')
        hashKey %= self.tableSize

        return hashKey
    
    # hash key에 해당하는 주소에 key : value 쌍 저장
    def add_hash(self, key, value):
        hashKey = self.get_hash_key(key)

        if self.hashTable[hashKey] == None:
            self.hashTable[hashKey] = {key, value}
            print(
                "hashKey 주소: ", hashKey, 
                "위치에 key:", key, 
                ",Value:", value, "이 저장 되었습니다."
                )
            
        else:
            _next = (hashKey + 1) % self.tableSize

            while self.hashTable[_next]:
                _next = (hashKey + 1) % self.tableSize

                if _next == hashKey:
                    print("빈 테이블이 없습니다.")
                    return 
                
            self.hashTable[_next] = {key, value}
            print(
                "hashKey 주소: ", hashKey, 
                "위치에 key:", key, 
                ",Value:", value, "이 저장 되었습니다."
                )
    
    # value 불러오기
    def get_value(self, key):
        hashKey = self.get_hash_key(key)

        if key in self.hashTable:
            return self.hashTable[hashKey]
        
        else:
            _next = (hashKey + 1) % self.tableSize
            
            while key not in self.hashTable:
                _next = (hashKey+1) % self.tableSize

                if _next == hashKey: 
                    print("해당 ",key,"의 값을 찾지 못했습니다.")
                    return 
                
            return self.hashTable[_next]
        

myHashTable = LinearProbingHash(10)
myHashTable.add_hash("abc",10)
myHashTable.add_hash("cba",20)
print("key 값 abcd의 value는 ",myHashTable.get_value("abcd"))
print("key 값 cbaf의 value는 ",myHashTable.get_value("cbaf"))
        

