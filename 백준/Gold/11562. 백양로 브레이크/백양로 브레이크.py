import sys
input = sys.stdin.readline
N,M = map(int,input().split())
INF = int(1e9)
dist = [[INF] * (N+1) for _ in range(N+1)]
for i in range(1,N+1):
    dist[i][i] = 0
for _ in range(M):
    u,v,b = map(int,input().split())
    dist[u][v] = 0
    dist[v][u] = 1-b

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])
K = int(input())
for _ in range(K):
    s,e = map(int,input().split())
    print(dist[s][e])