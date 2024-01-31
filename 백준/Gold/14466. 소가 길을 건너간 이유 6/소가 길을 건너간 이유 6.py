import sys
input = sys.stdin.readline
N,K,R = map(int,input().split())
roads = set([tuple(map(int,input().split())) for _ in range(R)])
cows = [tuple(map(int,input().split())) for _ in range(K)]
MAP = {t:n for n, t in enumerate(cows)}
inbound = lambda x,y: 0<x<=N and 0<y<=N
def dfs(x,y, n):
    visited = set([(x,y)])
    s = [(x,y)]
    cnt = 0
    while s:
        x,y = s.pop()
        if MAP.get((x,y)) and MAP[(x,y)] > n: cnt += 1
        for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
            nx, ny = x+dx, y+dy
            if not inbound(nx, ny) or (nx, ny) in visited: continue
            if (x,y,nx,ny) in roads or (nx,ny,x,y) in roads: continue
            s.append((nx,ny))
            visited.add((nx,ny))
    return cnt
answer = 0
for pos, n in MAP.items():
    a = dfs(*pos, n)
    answer += K - 1 - n - a
print(answer)