import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(3000000)
N = int(input())
inbound = lambda x,y: 0<=x<h and 0<=y<w
INF = 100000


def mkMap(q):
    t = []
    heapq.heapify(q)
    visited = set()
    fromOutDistMap = [[MAP[i][j] if MAP[i][j] == "*" else INF for j in range(w)] for i in range(h)]
    while q:
        d, x, y = heapq.heappop(q)
        if(x,y) in visited: continue
        visited.add((x,y))
        fromOutDistMap[x][y] = d
        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
            nx, ny = x + dx, y+dy
            if not inbound(nx, ny) or MAP[nx][ny] == "*" or (nx,ny)in visited: continue
            if MAP[nx][ny] != "#": heapq.heappush(q, (d,nx,ny))
            else: heapq.heappush(q, (d+1,nx,ny))
    return fromOutDistMap
for _ in range(N):
    h,w = map(int,input().split())
    MAP = [list(input().strip()) for _ in range(h)]
    pos = [(i,j) for i in range(h) for j in range(w) if MAP[i][j] == "$"]
    fromOutDistMap = mkMap([(MAP[i][j] == "#", i,j) for i in (0, h-1) for j in range(w) if MAP[i][j] != "*"] + [(MAP[i][j] == "#", i,j) for i in range(1, h-1) for j in (0, w-1) if MAP[i][j] != "*"])
    fromADistMap = mkMap([(0,*pos[0])])
    fromBDistMap = mkMap([(0,*pos[1])])
    dist = fromOutDistMap[pos[0][0]][pos[0][1]] + fromOutDistMap[pos[1][0]][pos[1][1]]
    for i in range(h):
        for j in range(w):
            if MAP[i][j] != "#" or fromOutDistMap[i][j] == "*" or fromADistMap[i][j] == "*" or fromBDistMap[i][j] == "*": continue
            dist = min(dist, fromOutDistMap[i][j] + fromADistMap[i][j] + fromBDistMap[i][j]-2)
    print(dist)