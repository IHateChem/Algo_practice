import sys
input =sys.stdin.readline
N=int(input())
M=int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
plan = list(map(lambda t: int(t)-1,input().split()))
parent = [i for i in range(N)]
def union(x, y):
    parent_x = find(x)
    parent_y = find(y)
    parent[parent_y] = parent_x
def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]
for i, isconnecteds in enumerate(graph):
    for n, isconnected in enumerate(isconnecteds[1+i:]):
        if isconnected:
            union(i, i+n+1)
plan_root = find(plan[0])
for site in plan:
    if plan_root != find(site): break
else:
    print("YES")
    exit(0)
print("NO")