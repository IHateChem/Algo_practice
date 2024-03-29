import sys
input = sys.stdin.readline
# 1. 먼저 각 지점에서 종료지점까지 거리를 구한다. 
INF = 100000000
N, M = map(int,input().split())
MAP = [input().strip() for _ in range(N)]
start2wall = [[INF]*M for _ in range(N)]
end2wall = [[INF]*M for _ in range(N)]
inbound = lambda x, y : 0<=x<N and 0<=y<M
def getDist(x, y, Map):
    dist = 0
    q = [(x,y,0)] # 좌표, 벽부순횟수
    visited = set([(x,y)])
    t = []
    while q:
        x,y,n = q.pop()
        Map[x][y] = dist
        if not n:
            for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
                nx, ny = x + dx, y +dy
                if not inbound(nx, ny) or (nx, ny) in visited: continue
                visited.add((nx,ny))
                t.append((nx, ny, int(MAP[nx][ny])))
        if not q:
            q = t
            t = []
            dist += 1
getDist(0,0, start2wall)
getDist(N-1,M-1, end2wall)
answer = INF
for i in range(N):
    for j in range(M):
        answer = min(start2wall[i][j] + end2wall[i][j], answer)
print(answer +1 if answer < INF else -1)