import sys
import heapq
input = sys.stdin.readline
answer = []
def waitTime(key,n, dir, lightInfo):
    total=lightInfo[key][1] + lightInfo[key][2]
    bias=lightInfo[key][0]
    t = n % total
    if dir == lightInfo[key][3]:
        if t < bias:
            return 0
        else:
            return total - t 
    else:
        if t < bias:
            return bias - t
        else:
            return 0

while 1:
    N,M=map(int,input().split())
    inbound=lambda x,y: 0<=x<N and 0<=y<M
    if not (N and M): break
    MAP=[list(input().strip()) for _ in range(N)]
    trafficLight=0
    for i in range(N):
        for j in range(M):
            if MAP[i][j]=="." or MAP[i][j]=="#":
                pass
            elif MAP[i][j] == "A":
                start=(i,j)
                MAP[i][j] = "#"
            elif MAP[i][j] == "B":
                end=(i,j)
                MAP[i][j] = "#"
            else:
                trafficLight += 1
    lightInfo={}
    for _ in range(trafficLight):
        t,d,a,b=input().strip().split()
        if d == "-":
            lightInfo[t] = (int(a),int(a),int(b),0)
        else:
            lightInfo[t] = (int(b),int(a),int(b),1)
    input()

    q=[(0, *start)]
    visited=set([start])
    record={start:0}
    while q:
        n,x,y = heapq.heappop(q)
        if (x,y)== end:
            answer.append(str(n))
            break
        for dx,dy in ((-1,0), (1,0),(0,-1),(0,1)):
            if inbound(x+dx,y+dy) and MAP[x+dx][y+dy] != ".":
                wait=0
                if MAP[x+dx][y+dy] != "#":
                    wait = waitTime(MAP[x+dx][y+dy] ,n, abs(dx), lightInfo)
                if (x+dx,y+dy) in visited and record[(x+dx,y+dy)] <= n+wait+1: continue
                visited.add((x+dx,y+dy))
                record[(x+dx,y+dy)] = n+wait+1
                heapq.heappush(q,(n+wait+1, x+dx,y+dy))
    else:
        answer.append("impossible")
print("\n".join(answer))