from collections import defaultdict as df
def solution(words, queries):
    TrieS = Node()
    answer = []
    TrieR = Node()
    for word in words:
        subTrieS = TrieS
        subTrieR = TrieR
        n = len(word)
        for i in range(n):
            subTrieS = subTrieS.addNext(word[i], n)
            subTrieR = subTrieR.addNext(word[n-i-1], n)
    for query in queries:
        if query[0] != "?":
            subTrie = TrieS
        else:
            subTrie = TrieR
            query = query[::-1]
        flag = True
        n = len(query)
        for q in query:
            if q == "?":
                answer.append(subTrie.lengths[n])
                flag = False
                break
            subTrie = subTrie.find(q)
            if not subTrie:
                answer.append(0)
                flag = False
                break
        if flag: answer.append(1)
    return answer
class Node:
    def __init__(self):
        self.lengths = df(int)
        self.next = {}
    def addNext(self, v, length):
        self.lengths[length] += 1
        n = self.next.get(v)
        if n:
            return n
        else:
            node = Node()
            self.next[v] = node
            return node
    def find(self, v):
        return self.next.get(v)