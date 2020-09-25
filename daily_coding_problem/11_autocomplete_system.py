"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

class TrieNode:
    def __init__(self):
        self.isEndOfWord = False
        self.children = [None]*26

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for level in word:
            index = ord(level) - ord('a')
            if not root.children[index]:
                root.children[index] = TrieNode()
            root = root.children[index]
        root.isEndOfWord = True

    def searchPrefix(self, prefix):
        root = self.root
        for level in prefix:
            index = ord(level) - ord('a')
            if not root.children[index]:
                return False
            root = root.children[index]
        return root

    def printNodes(self, root, string):
        if root.isEndOfWord:
            print(string)
            return
        for i in range(26):
            if root.children[i]:
                c = chr(i+ord('a'))
                self.printNodes(root.children[i], string+c)


if __name__ == '__main__':
    trie = Trie()
    words = ["dog", "deer", "deal"]
    for w in words:
        trie.insert(w)
    node = trie.searchPrefix("de")
    if node:
        trie.printNodes(node, "de")

