class TrieNode:
    def __init__(self):
        self.children = {}  # dict for save child node
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()  # root is a empty dict

    def insert(self, word):
        node = self.root  # start from root
        for char in word:
            # if char not in node, create new node with current char
            if char not in node:
                node.children[char] = TrieNode()
            # move to current node of current character
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            # if not exist in node, return False
            if char not in node.children:
                return False
            # move to node of current character
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
