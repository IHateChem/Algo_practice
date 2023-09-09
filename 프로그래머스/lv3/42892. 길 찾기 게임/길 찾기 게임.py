import heapq
from collections import defaultdict as dd
import sys
sys.setrecursionlimit(1000000)
class Node:
    def __init__(self, value,pos):
        self.value = value
        self.pos = pos
        self.left = None
        self.right= None
    def setLeft(self,nodeL):
        self.left=nodeL
    def setRight(self,nodeR):
        self.right=nodeR
def solution(nodeinfo):
    q = []
    floor = dd(list)
    def makeTree(nv:set, root:Node):
        rx,ry = root.pos
        left=set()
        leftq=[]
        right=set()
        rightq=[]
        for n in nv:
            x,y = nodeinfo[n-1]
            if x < rx:
                left.add(n)
                leftq.append((y,x,n))
            else:
                right.add(n)
                rightq.append((y,x,n))
        if left:
            childLeft=max(leftq)[2]
            N=Node(childLeft,(nodeinfo[childLeft-1]))
            left.remove(childLeft)
            root.setLeft(N)
            if left: makeTree(left, N)
        if right:
            child = max(rightq)[2]
            N=Node(child ,(nodeinfo[child-1]))
            right.remove(child)
            root.setRight(N)
            if right: makeTree(right, N)

    for n in range(len(nodeinfo)):
        x,y=nodeinfo[n]
        q.append((y,x,n+1))
    y,x,n = max(q)
    notvisited=set(range(1,len(nodeinfo)+1))
    notvisited.remove(n)
    rootNode = Node(n,(x,y))
    makeTree(notvisited, rootNode)
    def preOrder(N: Node, ret:list):
        ret.append(N.value)
        if N.left: preOrder(N.left, ret)
        if N.right: preOrder(N.right, ret)
    def postOrder(N: Node, ret:list):
        if N.left: postOrder(N.left, ret)
        if N.right: postOrder(N.right, ret)
        ret.append(N.value)
    answer = [[],[]]
    preOrder(rootNode,answer[0])
    postOrder(rootNode,answer[1])
    return answer