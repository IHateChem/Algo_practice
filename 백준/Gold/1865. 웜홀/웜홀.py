import sys
input = sys.stdin.readline
tc = int(input())   
INF = int(1e10)
for _ in range(tc):
    N,M,W = map(int,input().split())
    roads = [{} for _ in range(N+1)]
    for i in range(M):
        S,E,T = map(int,input().split())
        if E in roads[S]:
            roads[S][E] = min(roads[S][E],T)
            roads[E][S] = min(roads[E][S],T)
        else:
            roads[E][S] = T
            roads[S][E] = T
    for i in range(W):
        S,E,T = map(int,input().split())
        if E in roads[S]:
            roads[S][E] = min(roads[S][E],-T)
        else:
            roads[S][E] = -T
    dist = [INF] *(N+1)
    dist[0] = 0
    for __ in range(N-1):
        for j in range(1,N+1):
            for k in roads[j].keys():
                if dist[k] > dist[j] + roads[j][k]:
                    dist[k] = dist[j] + roads[j][k]
    checkSum = sum(dist)
    for j in range(1,N+1):
        for k in roads[j].keys():
            if dist[k] > dist[j] + roads[j][k]:
                dist[k] = dist[j] + roads[j][k]
    if checkSum > sum(dist):
        print("YES")
    else: print("NO")