#아이디어: 모든 늑대노드는 얻을 수 있는 최대 점수의 음수값, 양과의 거리를 기록
#그후 그리디하게 찾아나간다. 
import heapq
class Node:
    def __init__(self, idx, animal):
        self.idx = idx
        self.animal = animal
        self.parent = None
        self.left = None
        self.right = None
    def getChildren(self):
        return filter(lambda t: t, [self.left, self.right])
SHEEP = 0
WOLF = 1
def calc(nodes, score, sheeps):
    ret = sheeps
    for node in nodes:
        _score, _sheeps = score, sheeps
        if node.animal is SHEEP:
            _score += 1
            _sheeps += 1
        else:
            _score -= 1
        if not _score: continue
        ret = max(ret, calc([n for n in nodes if n != node] + list(node.getChildren()),_score, _sheeps))
    return ret
def solution(info, edges):
    N = len(info)
    answer = 1
    leaves = set(range(N))
    Nodes = [Node(i, info[i]) for i in range(N)]
    for u, v in edges:
        if u in leaves: leaves.remove(u)
        if Nodes[u].left:
            Nodes[u].right = Nodes[v]
        else:
            Nodes[u].left = Nodes[v]
        Nodes[v].parent = Nodes[u]
    return calc([Nodes[0]], 0,0)