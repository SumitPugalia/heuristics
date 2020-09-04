words = ["cd", "ad", "ada", "ef", "cat"]
wordTree = dict()

def make_trie(words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict['$'] = '$'
    return root

def makeTree(wordTree, word):
    if not word:
        return {'$': '$'}
    
    if word[0] in wordTree:
        innerWordTree = wordTree[word[0]]
        n = makeTree(innerWordTree, word[1:])
        innerWordTree.update(n)
        wordTree[word[0]] = innerWordTree
        innerWordTree = wordTree
    else:
        innerWordTree = dict()
        innerWordTree[word[0]] = makeTree(innerWordTree, word[1:])
    return innerWordTree


print("MAKE TIE:", make_trie(words))

for word in words:
    wordTree.update(makeTree(wordTree, word))

print("Final", wordTree)

# from collections import defaultdict
# class StreamChecker:

#     def __init__(self, words: List[str]):
#         self.wordTree = defaultdict()
        
#         def makeTree(wordTree, word):
#             if not word:
#                 return "$"
#             if word[0] not in wordTree:
#                 innerWordTree = dict()
#             else:
#                 innerWordTree = wordTree[word[0]]
            
#             innerWordTree[word[0]] = makeTree(innerWordTree, word[1:])
#             return innerWordTree
        
#         for word in words:
#             self.wordTree[word[0]] = makeTree(self.wordTree, word[1:])
#         print(self.wordTree)
                
#     def query(self, letter: str) -> bool:
#         if letter in self.wordTree:
#             value = self.wordTree[letter]
#             if value == '$':
#                 return True
#             else:
#                 del self.wordTree[letter]
#                 for k, v in value.items():
#                     self.wordTree[k] = v
#         return False



