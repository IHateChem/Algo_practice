import sys
sys.setrecursionlimit(1000000)
class Trie:
    def __init__(self, v):
        self.value = v
        self.child = {}
        self.score = 0
    def insert(self, string):
        w = string.pop()
        if self.child and not self.child.get(w):
            self.score = 1
        if not self.child.get(w): self.child[w] = Trie(w)
        self.score += 1 
        if string:
            self.child[w].insert(string)
        else:
            self.child[w].child["fin"] = None
    def find(self, string, n):
        w = string.pop()
        if self.score > 1:
            n += 1
            if string: n = self.child[w].find(string, n)
        return n 
        
            
def solution(words):
    answer = 0
    words.sort()
    if len(words) == 1: return 1
    T = Trie("root")
    for word in words:
        word = list(word[::-1])
        T.insert(word)
    for word in words:
        word = list(word[::-1])
        answer += T.find(word, 0)
    return answer