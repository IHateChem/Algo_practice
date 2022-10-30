'''
아이디어: 
1단계: 맵에서 섬에 번호 매기기. (왼쪽 위에 있을 수록 작은 숫자.)
2단계: 1번섬부터 naive하게 다리 찾기. (아래랑 오른쪽만 봐도될듯)
3단계: 딕셔널리에 다리길이 저장하기. key는 set으로 설정. 

'''
from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
prime = [2,3, 5, 7, 11, 13]
getindex = {
    2 : 0,
    3: 1,
    5: 2,
    7 : 3,
    11 : 4,
    13 : 5 
}
rsa ={
    6: (2, 3),
    10: (2, 5),
    14: (2, 7),
    22: (2, 11),
    26: (2, 13),
    15: (5, 3),
    21: (7, 3),
    33: (11, 3),
    39: (13, 3),
    35: (5, 7),
    55: (5, 11),
    65: (5, 13),
    77: (11, 7),
    91: (13, 7),
    143: (11, 13),
}
N, M = map(int, input().split())
location = []
bridge = defaultdict(int)
whereis = defaultdict(int)
islandindex = 0
for _ in range(N):
    t = list(map(int, input().split()))
    location.append(t)
x = 0; y = 0;
def coloringisland(x, y):
    location[x][y] = prime[islandindex]
    if (x-1) >= 0:
        if location[x-1][y] == 1:
            coloringisland(x-1, y)
    if (x+1) < N:
        if location[x+1][y] == 1:
            coloringisland(x+1, y)
    if (y-1) >= 0:
        if location[x][y-1] == 1:
            coloringisland(x, y-1)
    if (y+1) < M:
        if location[x][y+1] == 1:
            coloringisland(x, y+1)
    return islandindex + 1
for n in range(N):
    for m in range(M):
        if location[n][m] == 1:
            whereis[islandindex] = (n, m)
            islandindex = coloringisland(n, m)
for n in range(N):
    p = 0
    for m in range(M):
        if location[n][m] != 0:
            if p == 0:
                p = location[n][m]
            if location[n][m] == p:
                t = m
            elif location[n][m] != p:   
                s = p * location[n][m]
                if (not bridge[s] or bridge[s] > m - t -1) and (m-t) > 2:
                    bridge[s] = m - t -1
                p = location[n][m]
                t = m
for m in range(M):
    p = 0
    for n in range(N):
        if location[n][m] != 0:
            if p == 0:
                p = location[n][m]
            if location[n][m] == p:
                t = n
            elif location[n][m] != p:
                s = p * location[n][m]
                if  (not bridge[s] or bridge[s] > n - t -1) and (n-t) > 2:
                    bridge[s] = n - t -1
                p = location[n][m]
                t = n
bridges = sorted(list(bridge.items()))
stack = []
for p, b in bridges:
    u, v = rsa[p]
    heapq.heappush(stack, (b, getindex[u], getindex[v]))
visited = [0]*(islandindex)
answer = 0
count = 0
parent =  [i for i in range(islandindex)]
unionset = [[] for _ in range(islandindex)]
while stack:
    b, u, v = heapq.heappop(stack)
    if b > 1:
        if visited[u]:
            if visited[v]:
                if parent[u] != parent[v]:
                    for uniset in unionset[parent[u]]:
                        parent[uniset] = parent[v]
                        unionset[parent[v]].append(uniset)
                    unionset[parent[u]] = []
                    parent[u] = parent[v]
                    unionset[parent[v]].append(u)
                    count += 1
                    answer += b
            else:
                visited[v] = 1
                parent[v] = parent[u]
                count += 1
                answer += b
                unionset[parent[u]].append(v)
        else:
            count += 1
            if visited[v]:
                visited[u] = 1
                parent[u] = parent[v]
                unionset[parent[v]].append(u)
                answer += b
            else:
                visited[u] = 1
                visited[v] = 1
                parent[u] = parent[v]
                unionset[parent[v]].append(u)
                answer += b
    if count == (islandindex-1):
        break
for i in visited:
    if not i:
        print(-1)
        break
else:
    if count != (islandindex-1):
        print(-1)
    else:
        print(answer)