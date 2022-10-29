import sys
input = sys.stdin.readline
N = int(input())
treedept = {}
tree = [[] for _ in range(N+1)]
notin = []
treedept[1] = 1
for i in range(N-1):
    u, v = map(int, input().split())
    tree[v].append(u)
    tree[u].append(v)

visited = [0] *(N+1)
parent = [0] *(N+1)
stack = [(1,0)]
dept = 1
tempset = []
while stack:
    t , p= stack.pop()
    visited[t] = dept
    parent[t] = p
    for next in tree[t]:
        if not visited[next]:
            tempset.append((next, t))
    if not stack:
        dept += 1
        stack = tempset
        tempset = []
M = int(input())
def getlca(u,v):
    dept_u = visited[u]
    dept_v = visited[v]
    flag = dept_u < dept_v
    if flag: 
        for i in range(dept_v-dept_u):  v = parent[v]
    else:
        for i in range(dept_u-dept_v):  u = parent[u]
    while 1:
        if u == v:
            break
        v = parent[v]
        u = parent[u]
    return u
a = []
for _ in range(M):
    u, v = map(int, input().split())
    a.append(str(getlca(u,v)))
print("\n".join(a))