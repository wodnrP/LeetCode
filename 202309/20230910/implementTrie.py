class Node:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        self.root = Node()
    

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = Node()

            curr = curr.children[i]
        curr.isEndOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return curr.isEndOfWord


    def startsWith(self, prefix: str):
        curr = self.root
        for i in prefix:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return True