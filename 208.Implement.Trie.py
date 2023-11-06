class Trie:
    def __init__(self):
        self.trie_word = ''

    def insert(self, word: str) -> None:
        self.trie_word = word

    def search(self, word: str) -> bool:
        
        if len(word) != len(self.trie_word):
            return False
        else:
            result = False
            for idx in range(len(word)):
                if self.trie_word[idx] == word[idx]:
                    result = True
                else:
                    return False
            return result 

    def startsWith(self, prefix: str) -> bool:
        result = False
        for idx in range(len(prefix)):
            print(self.trie_word[0])
            if prefix[idx] == self.trie_word[idx]:
                result = True
            else:
                return False
        return result

if __name__ == "__main__":
    obj = Trie()
    obj.insert('apple')
    param_2 = obj.search('apple')
    param_3 = obj.startsWith('app')

    print(param_2)
    print(param_3)