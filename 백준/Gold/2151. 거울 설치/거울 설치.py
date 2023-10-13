import sys
input=sys.stdin.readline
n=int(input())
MAP=[list(input().strip())for _ in range(n)]
s, e = ((i,j) for i in range(n) for j in range(n) if MAP[i][j] == "#")
dir=[(1,0),(0,1),(-1,0),(0,-1)]
nextDir=[[3,0,1,2],[1,2,3,0]]
q=[(*s,i) for i in range(4)]
inbound = lambda nx,ny: 0<=nx<n and 0<=ny<n and MAP[nx][ny] != "*"
answer = 0
t=[]
while q:
    x,y,d = q.pop()
    for i in range(n):
        dx,dy=dir[d]
        x += dx
        y += dy
        if not inbound(x,y): break
        if MAP[x][y] == "!":
            for k in range(2):
                t.append((x,y,nextDir[k][d]))
        elif (x,y)==e:
            t = []
            q = []
            answer -= 1
            break 
    if not q:
        answer += 1
        q = t
        t = []
print(answer)