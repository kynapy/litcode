# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/
# Attempts: 1


class Trie:
    def __init__(self):
        self.map = {}

    def insert(self, word: str) -> None:
        curr = self.map
        for i in word:
            if not i in curr:
                curr[i] = {}
            curr = curr[i]
        curr["\n"] = "\n"

    def search(self, word: str) -> bool:
        curr = self.map
        for i in word:
            if i in curr:
                curr = curr[i]
            else:
                return False
        if "\n" in curr:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.map
        for i in prefix:
            if i in curr:
                curr = curr[i]
            else:
                return False
        return True


### TEST CASES
obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
obj.insert("app")
print(obj.search("app"))
