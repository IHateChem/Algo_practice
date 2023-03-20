class node:
    def __init__(self):
        self.value = ""
        self.children = defaultdict(int)
        self.isfinish = False
    def setvalue(self, w:str) -> None:
        self.value = w
        return self
    def setchild(self, w:str) ->None:
        N = node().setvalue(w)
        self.children[w] = N
        return N
class Trie:
    def __init__(self):
        self.roots = defaultdict(int)
    def insert(self, word: str) -> None:
        N = self.roots
        for i, w in enumerate(word):
            if N[w]:
                if i == len(word)-1:
                    N[w].isfinish = True
                N = N[w].children
            else:
                newnode = node().setvalue(w)
                N[w] = newnode
                if i == len(word)-1:
                    N[w].isfinish = True
                N =  newnode.children

    def search(self, word: str) -> bool:
        N = self.roots
        for w in word:
            flag = False
            if N[w]:
                flag = N[w].isfinish
                N = N[w].children
            else:break
        else:
            if flag: return True
        return False        

    def startsWith(self, prefix: str) -> bool:
        N = self.roots
        for w in prefix:
            if N[w]:
                N = N[w].children
            else:break
        else:
            return True
        return False   


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix);k
