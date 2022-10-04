''''
아이디어: 가중치에 음수를 곱해 저장후 벨만포드 진행, 끝나고 모든 엣지 돌면서 가중치 업데이트 되면 -1
시간: O EV
구현: 그래프: 어레이리스트 방식. 
'''
import copy
import sys
input = sys.stdin.readline
INF = 10**10
N, M = map(int,input().strip().split())
graph = [[] for _ in " "*(N+1)]
edge = []
path =  [0] *(N+1)
distance =  [INF]*(N+1)
neggroup = {}
for _ in " "*M:
    u, v, w = map(int, input().strip().split())
    w *= -1
    graph[u].append(v)
    edge.append((u, v, w))
#벨만포드 시작
distance[1]  = 0
Tdistance =  copy.deepcopy(distance)
for _ in range(N):
    for u, v, w in edge:
        if distance[u] < INF and distance[v] > distance[u] + w:
            path[v] = u
            distance[v] =  distance[u] + w
for u, v, w in edge:
    if distance[u] < INF and distance[v] > distance[u] + w:
        neggroup[v] = 1
visited = [0]*(N+1)
stack = list(neggroup.keys())
while stack:
    v = stack.pop()
    neggroup[v] = 1
    for u in graph[v]:
        if not visited[u]:
            stack.append(u)
            visited[u] = 1
else:
    p = N
    route = []
    for _ in " "*M:
        if neggroup.get(p) or p == 0:
            break
        route.append(p)
        p = path[p]
    if 1 in route:
        print(" ".join(map(str, route[::-1])))
    else:
        print(-1)