import heapq
import sys
input=sys.stdin.readline
N,M,T,D = map(int,input().split())
alpha2idx = {chr(i+65):i  for i in range(26)}
alpha2idx.update( {chr(i+97):i+26  for i in range(26)})
MAP = [list(map(lambda t: alpha2idx[t], input().strip())) for _ in range(N)]
answer =0
outbound = lambda x, y, t: not (0<=x<N and 0<=y<M and abs(t - MAP[x][y]) <= T)
getDist = lambda x, y : (y-x) ** 2 if y > x else 1

comeback = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited = [[0]*M for _ in range(N)]
        stack = [(0, i, j)]
        while stack:
            t, n, m = heapq.heappop(stack)
            if n == 0 and m == 0: break
            if visited[n][m]: continue
            visited[n][m] = 1
            height = MAP[n][m]
            for dn, dm in ((1,0), (-1,0), (0,1),(0,-1)):
                if outbound(n+dn, m+dm, height) or visited[n+dn][m+dm]: continue
                heapq.heappush(stack, (t + getDist(height, MAP[n+dn][m+dm]),n+dn,m+dm))
        comeback[i][j] = t + comeback[n][m]
stack = [(0, 0,0)]
visited = [[0]*M for _ in range(N)]
while stack:
    t, n, m = heapq.heappop(stack)
    if visited[n][m]: continue
    visited[n][m] = 1
    height = MAP[n][m]
    answer= max(answer, height)
    for dn, dm in ((1,0), (-1,0), (0,1),(0,-1)):
        if outbound(n+dn, m+dm, height) or visited[n+dn][m+dm]: continue
        if t + getDist(height, MAP[n+dn][m+dm]) + comeback[n+dn][m+dm]<= D:
            heapq.heappush(stack, (t + getDist(height, MAP[n+dn][m+dm]),n+dn,m+dm))
print(answer)   
