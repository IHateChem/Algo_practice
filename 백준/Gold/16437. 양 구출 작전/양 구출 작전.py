import sys
input=sys.stdin.readline
N=int(input())
TREE=[["S",0,1],["S",0,0]]
ReverseTree = [[] for _ in range(N+1)]
for i in range(N-1):
    t,a,p=input().strip().split()
    TREE.append([t,int(a) if t =="S" else -int(a), int(p)])
    ReverseTree[int(p)].append(i+2)
q = [1];dept=0;deptList=[[]];t=[]
while q: #bfs
    n=q.pop()
    deptList[dept].append(n)
    for child in ReverseTree[n]:
        t.append(child)
    if not q:
        q = t
        t = []
        dept += 1
        deptList.append([])
for nodes in deptList[::-1]:
    for node in nodes:
        t,a,p=TREE[node]
        if t == "W" and a <0: continue
        TREE[p][1] += a
print(TREE[0][1])