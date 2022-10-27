import sys
input = sys.stdin.readline
N = int(input())
id = 1
Tree = [ [] for _ in range(N+1)]
for i in range(N-1):
    u, v = map(int, input().split())
    Tree[u].append(v)
    Tree[v].append(u)
orderlist = []
stack = [1]
visited = [0] * (N+1)
while stack:
    t = stack.pop()
    visited[t] = 1
    orderlist.append(t)
    for child in Tree[t]:
        if not visited[child]:
            stack.append(child)
            visited[child] = 1
dynamicN = [0] * (N+1)
dynamic = [0]*(N+1)
visited = [0] * (N+1)
for order in list(orderlist)[::-1]:
    visited[order] = 1
    dynamic[order] += 1
    for child in Tree[order]:
        if visited[child]:
            dynamic[order] += min(dynamicN[child],dynamic[child])
            dynamicN[order] += dynamic[child]
answer = min(dynamic[order], dynamicN[order])
print(answer)