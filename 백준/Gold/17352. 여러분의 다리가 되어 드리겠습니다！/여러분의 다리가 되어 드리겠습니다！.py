import sys
input=sys.stdin.readline

N = int(input())
parent = [i for i in range(N+1)]
def union(u, v):
    parent_u, parent_v= sorted([find(u),find(v)])
    parent[parent_u] = parent_v
def find(u):
    if parent[u] != u:
        parent_u = find(parent[u])
        parent[u] = parent_u
    return parent[u]

for _ in range(N-2):
    u, v = map(int,input().split())
    union(u,v)
for i in range(1,N):
    find(i)
islands = set(parent)
islands.remove(0)
print(*islands)