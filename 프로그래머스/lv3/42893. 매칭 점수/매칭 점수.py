import re
class Node:
    def __init__(self):
        self.isEnd = False
        self.table = {}
    def goNext(self, v, n):
        N = self.table[v]
        if self.isEnd and v == "NA":
            return n+1, N
        else:
            return n, N
alphabet = set([chr(97+i) for i in range(26)])
def Automata(word, page):
        start = Node() 
        word=word.lower()
        nodeNext = Node() #Not Alphabet
        wordSet = set(word)
        for w in alphabet:
            start.table[w] = start
        start.table["NA"] = nodeNext
        node = nodeNext; node.table["NA"] =node
        for w in word:
            N = Node()
            for a in alphabet:
                if a == w:
                    node.table[a] = N
                else:
                    node.table[a] = start
            N.table["NA"] = nodeNext
            node = N
        for a in alphabet:
            N.table[a] = start
        N.isEnd = True
        node = start
        answer = 0
        for p in page.lower():
            if not p in alphabet:
                p = "NA"
            answer, node = node.goNext(p,answer)
        return answer
def parser(page,word):
    score= Automata(word, page)
    url = re.search(r'(<meta property.+content=")(https://.*)"/>', page).group(2) 
    links = re.findall(r'<a href="(https://\S*)">', page) 
    return score, url, links
def solution(word, pages):
    info = [];idx=0
    link2idx={}
    for page in pages:
        score, url, links = parser(page,word)
        info.append((score, url, links))
        link2idx[url]=idx
        idx+=1
    answer = 0; answerIdx=0
    finalscore=[0]*idx
    for i in range(idx):
        finalscore[i] += info[i][0]
        for link in info[i][2]:
            if link2idx.get(link) == None: continue
            finalscore[link2idx[link]] += info[i][0] / len(info[i][2])
    for i in range(idx):
        if answer < finalscore[i]:
            answer = finalscore[i]
            answerIdx=i
    return answerIdx