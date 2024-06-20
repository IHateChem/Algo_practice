import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
A = list(map(int,input().split()))

parent =[0] + [i+1 for i in range(N)]

def union(a,b):
    pa = find(a)
    pb = find(b)
    pa, pb = min(pa, pb), max(pa, pb)
    parent[pb] = pa
def find(a):
    if a == parent[a]: return a
    pa = find(parent[a])
    parent[a] = pa
    return pa
for _ in range(M):
    v,w = map(int,input().split())
    v,w = min(v,w), max(v,w)
    union(v,w)
for i in range(N):
    find(i+1)
setP = set(parent)
groups = [1000000000 if i in setP and i else 0 for i in range(N+1)]
for i in range(N):
    pa = parent[i+1]
    groups[pa] = min(groups[pa], A[i])
answer = sum(groups)
print(answer if answer <= K else "Oh no")