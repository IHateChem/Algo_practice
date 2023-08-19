INF=10000000000000
def solution(n, s, a, b, fares):
    dist = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(n): dist[i+1][i+1]= 0
    for i,j, f in fares:
        dist[i][j] = f
        dist[j][i] = f
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
    answer = INF
    for i in range(n+1):
        answer=  min(answer, dist[s][i] + dist[i][a] + dist[i][b])
    return answer