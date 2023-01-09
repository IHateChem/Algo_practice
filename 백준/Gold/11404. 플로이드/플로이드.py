import sys
input = sys.stdin.readline
INF = 1e8
N = int(input())
M = int(input())
dist = [[INF if i != j else 0 for j in range(N+1)] for i in range(N+1)]
for _ in range(M):
    a, b, c= map(int, input().split())
    dist[a][b] = min(c, dist[a][b])
def floyd(n):
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                dist[j][k] = min(dist[j][i] + dist[i][k], dist[j][k])
floyd(N)
for i in dist[1:]:
    answer = []
    for j in i[1:]:
        if j == INF:
            answer.append("0")
        else: answer.append(str(j))
    print(" ".join(answer))