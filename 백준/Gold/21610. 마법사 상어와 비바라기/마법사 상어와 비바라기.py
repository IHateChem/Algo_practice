#푸는중
import sys
input = sys.stdin.readline
directions = [(),(0,-1),(-1,-1), (-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
N,M=map(int,input().split())
MAP=[list(map(int,input().split())) for _ in range(N)]
clouds = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]
def waterCopy(x, y):
    ret = 0
    if x -1>=0 and y-1>=0: ret += bool(MAP[x-1][y-1])
    if x -1>=0 and y+1<N: ret += bool(MAP[x-1][y+1])
    if x +1<N and y-1>=0: ret += bool(MAP[x+1][y-1])
    if x +1<N and y+1<N: ret += bool(MAP[x+1][y+1])
    return ret
for _ in range(M):
    d,s=map(int, input().split())
    past = set()
    for i in range(len(clouds)):
        clouds[i][0] = (clouds[i][0] + directions[d][0]*s) % N
        clouds[i][1] = (clouds[i][1] + directions[d][1]*s) % N
    for cx, cy in clouds:
        MAP[cx][cy] += 1
        past.add((cx,cy))
    for cx, cy in clouds:
        MAP[cx][cy] += waterCopy(cx,cy)
    clouds = []
    for i in range(N):
        for j in range(N):
            if MAP[i][j] >= 2 and (not (i,j) in past):
                MAP[i][j] -= 2
                clouds.append([i,j])
answer = 0
for i in range(N):
    answer += sum(MAP[i])
print(answer)