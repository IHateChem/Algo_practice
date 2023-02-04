'''
아이디어: 매 시행마다 떨어지는 리프노드는 정해져있음. -> 횟수를 알 수 있음.
dp?로   시행 \ 숫자로 슥삭.
'''
from collections import deque
class node:
    def __init__(self, v):
        self.isroot = False
        self.value = v
        self.children = set()
        self.connected = 0
    def set_connect(self):
        _min = 101
        if not len(self.children): return
        if len(self.children) == 1:
            self.connected = list(self.children)[0]
            return
        if self.connected == max(self.children):
            self.connected = min(self.children)
            return
        for child in self.children:
            if child > self.connected and child < _min:
                _min = child
        self.connected= _min
def setting_default_connect(n):
    nodes[n].set_connect()
    for child in nodes[n].children:
        setting_default_connect(child)
def buildtree(edges):
    for parent, child in edges:
        nodes[parent].children.add(child)
    setting_default_connect(1)
def getNextConnect(n):
    if not nodes[n].children: return n
    next = nodes[n].connected
    nodes[n].set_connect()
    return getNextConnect(next)
nodes = [node(_) for _ in range(101)]
def get_distribution(i, n):
    ret = deque()
    while n and i:
        if 3*i - n > 1:
            ret.append(1)
            n -= 1
        elif 3*i - n == 1:
            n -= 2
            ret.append(2)
        else:
            n -= 3
            ret.append(3)
        i -= 1
    return ret
    
def solution(edges, target):
    answer = []
    buildtree(edges)
    how_many_needs = [[t//3 if t % 3 == 0 else t//3 + 1, t] for t in target] #[min, max]
    how_many_advent = [0]*len(target)
    sequence = []
    how2distribute = [deque() for _ in target]
    while 1:
        flag = False
        n = getNextConnect(1)
        sequence.append(n)
        how_many_advent[n-1] += 1
        for t, need in zip(how_many_advent, how_many_needs):
            if t < need[0]:
                flag = True
                break
            if t > need[1]:
                return [-1]
        if flag: continue
        for n, i in enumerate(how_many_advent):
            how2distribute[n] = get_distribution(i, target[n])
        break
    answer = [how2distribute[n-1].popleft() for n in sequence]
    return answer
#초기엔 가장 작은 번호를 간선으로. 

#숫자가 리프노드에 도착하면 숫자가 지나간 노드는 다음으로 번호가 큰 자식 노드를 가르키는 갓너을 새로운길로 설정
#기존 길은 끊기
# -현재 길로 연결된 노드가 클시 ㅈ가은 노드를 가르키는 간선을 길로
# - 간선이 하나면 계속 하나의 간선을 길로 설정
# 계속 숫자 떨어트리기 가능. 리프노드까지 떨어진 후에는 새로운 숫자 떨어트려야함.
# target 과 같은 값

