import sys
from collections import deque
input = sys.stdin.readline
n = int(input().strip())

graph = []
levelup = [0,0,2,5,9,14,20,2**30]
eat = 0
size = 2
totdistance = 0
def BFS( pos):
    global graph
    x = pos[0]
    y = pos[1]
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    q = deque()
    q.append((x,y))
    t = []
    distance = 0
    while q:
        x,  y = q.popleft()
        global size
        if graph[x][y] and graph[x][y] < size:
            global eat
            graph[x][y] = 0
            eat += 1
            if eat >= levelup[size]:
                size += 1
            global position
            position = (x, y)
            return distance
        if x - 1 >= 0 and graph[x-1][y] <= size and not visited[x-1][y]:
            visited[x-1][y] = 1
            t.append((x-1,y))
        if y - 1 >= 0 and graph[x][y-1] <= size and not visited[x][y-1]:
            visited[x][y-1] = 1
            t.append((x,y-1))
        if y + 1 < n and graph[x][y+1] <= size and not visited[x][y+1]:
            t.append((x,y+1))
            visited[x][y+1] = 1
        if x + 1 < n and graph[x+1][y] <= size and not visited[x+1][y]:
            visited[x+1][y] = 1
            t.append((x+1,y))
        if not q:
            if t:
                t.sort()
                q = deque(t)
                distance += 1
                t = []
    return 0

for i in range(n):
    s = list(map(int, input().strip().split()))
    try:
        y = s.index(9)
        position = [i,y]
        s[y] = 0
    except:
        pass
    graph.append(s)  
state = 1
while state:
    state=  BFS(position)
    if not state:
        print(totdistance)
        break
    else:
        totdistance += state