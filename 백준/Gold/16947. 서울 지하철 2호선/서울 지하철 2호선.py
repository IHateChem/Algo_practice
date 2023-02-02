import sys
input = sys.stdin.readline
N = int(input())
nums = [0]*(N+1)
graph = [[] for _ in range(N+1)]
for _ in range(N):
    a,b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    nums[a] += 1
    nums[b] += 1
root = []
for n, i in enumerate(nums):
    if i == 1: root.append(n)
visited = [0]*(N+1)
crosspnts = []
branches = set()
for node in root:
    stack = [node]
    while stack:
        u = stack.pop()
        visited[u] = 1
        branches.add(u)
        for v in graph[u]:
            if not visited[v]:
                if nums[v] == 2:
                    stack.append(v)
                else:
                    crosspnts.append(v)
                    nums[v] -= 1
answer = [0]*(N+1)
visited = [0]*(N+1)
for pnt in crosspnts[::-1]:
    if visited[pnt]: continue
    stack = [pnt]
    p = -1
    t = []
    while stack:
        u = stack.pop()
        answer[u] = p + 1
        visited[u] = 1
        for v in graph[u]:
            if v in branches and not visited[v]:
                t.append(v)
        if not stack:
            stack = t
            p += 1
            t = []
print(" ".join(map(str, answer[1:])))