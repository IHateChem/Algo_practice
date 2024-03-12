import sys
N,M = map(int,input().split())
parent = [i for i in range(N+1)]
def union(a, b):
    p_a = find(a)
    p_b = find(b)
    p_a, p_b = sorted((p_a, p_b))
    parent[p_b] = p_a
def find(a):
    if a != parent[a]: parent[a] = find(parent[a])
    return parent[a]
for _ in range(M):
    a, b = map(int,input().split())
    a, b = sorted((a,b))
    union(a, b)
MAP = [list(map(int,input().split())) for _ in range(N)]
edges = []
for i in range(1, N):
    for j in range(i+1, N):
        edges.append((MAP[i][j], i+1, j+1))
edges.sort()
ans = 0
answer = []
for n, a, b in edges:
    if find(a) == find(b): continue
    ans += n
    union(a, b)
    answer.append(f"{a} {b}")
print(ans, len(answer))
for a in answer:
    print(a)