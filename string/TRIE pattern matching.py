# Python program for insert and search
# operation in a Trie

class TrieNode:
    def __init__(self):
        self.isEow = False
        self.child = [None]*26

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def getRoot(self):
        return self.root

    def insert(self, word):
        root = self.root
        for level in range(len(word)):
            idx = ord(word[level]) - ord('a')
            if not root.child[idx]:
                root.child[idx] = TrieNode()
            root = root.child[idx]
        root.isEow = True

    def printTrie(self, root, word=''):
        if not root:
            return
        if root.isEow:
            print(word)
        for i, child in enumerate(root.child):
            if child:
                self.printTrie(child, word+chr(97+i))

    def search(self, word, is_whole_word=True):
        root = self.root
        for level in range(len(word)):
            idx = ord(word[level]) - ord('a')
            if not root.child[idx]:
                return False
            root = root.child[idx]
        if not is_whole_word:
            return root
        return root and root.isEow

    def searchRegex(self, regex):
        node = self.search(regex, is_whole_word=False)
        if node:
            self.printTrie(node, regex)
        return None


# driver function
def main():

    # Input keys (use only 'a' through 'z' and lower case)
    keys = ['mohit', 'mohi', 'rohit', 'what', 'whatis']

    t = Trie()

    print('inserting keys ', keys)
    for key in keys:
        t.insert(key)

    # Search for words
    word = 'mohit'
    print('is "',word,'" present: ', t.search(word))

    # Print trie
    print('printing trie')
    t.printTrie(t.getRoot())

    regex = 'mohit*'
    print('regex:', regex)
    t.searchRegex(regex[:-1])

if __name__ == '__main__':
    main()
