import sys
import heapq
input=sys.stdin.readline
N=int(input())
W = []
for _ in range(N):
    W.append((int(input()), _))
P = []
for _ in range(N):
    P.append(map(int,input().split()))
visited = [0]*N
ispushed = [[0]*N for _ in range(N)]
stack = []
for j in W:
    heapq.heappush(stack, j)
answer=  0
while stack:
    t = heapq.heappop(stack)
    if visited[t[1]]: continue
    answer += t[0]
    visited[t[1]] = 1
    for n, j in enumerate(P[t[1]]):
        if not (ispushed[n][t[1]] or ispushed[t[1]][n]):
            heapq.heappush(stack, (j, n))
            ispushed[n][t[1]] =1
print(answer)