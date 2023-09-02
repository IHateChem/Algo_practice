import sys
input=sys.stdin.readline
INF=100000000000
N=int(input())
W=int(input())
dist=[[INF]*(W+1) for _ in range(W+1)]
dp=[[INF]*(W+1) for _ in range(W+1)]
positions=[[(1,1),(N,N)]]
def distance(pos1, pos2):
    if dist[pos1][pos2] != INF:
        return dist[pos1][pos2]
    x,y=positions[pos1]
    r,c=positions[pos2]
    if pos1 ==0:
        x,y = positions[0][0]
    elif pos2 == 0:
        r,c=positions[0][1]
    d = abs(x-r)+abs(y-c)
    dist[pos1][pos2]=d
    return d
x,y=map(int,input().split())
positions.append((x,y))
dp[0][1] = distance(1,0)
dp[1][0] = distance(0,1)
PATH=[[0]*(W+1) for _ in range(W+1)]
idx=1
for i in range(W-1):
    x,y=map(int,input().split())
    positions.append((x,y))
    for j in range(idx):
        d=distance(idx,idx+1)
        dp[idx+1][j] = dp[idx][j]+d
        d=distance(idx+1,idx)
        dp[j][idx+1] = dp[j][idx]+d
        PATH[idx+1][j] = 1
        PATH[j][idx+1] = 1
        d1=distance(j,idx+1)
        if dp[idx+1][idx] > dp[j][idx] + d1:
            dp[idx+1][idx] = dp[j][idx] + d1
            PATH[idx+1][idx] = idx+1-j
        d1=distance(idx+1,j)
        if dp[idx][idx+1] > dp[idx][j] + d1:
            dp[idx][idx+1] = dp[idx][j] + d1
            PATH[idx][idx+1] = idx+1-j
    idx+=1
answer=INF
for i in range(W+1):
    if answer > dp[-1][i]:
        answer = dp[-1][i]
        pos=[W,i]
        p = PATH[W][i]
    if answer > dp[i][-1]:
        answer = dp[i][-1]
        pos=[i, W]
        p = PATH[i][W]
print(answer)
answer=[]
while p:
    if pos[0]<pos[1]:
        answer.append(2)
        pos[1] -= p
    else:
        answer.append(1)
        pos[0] -= p
    p = PATH[pos[0]][pos[1]]
if pos[0]<pos[1]:
    answer.append(2)
    pos[1] -= p
else:
    answer.append(1)
    pos[0] -= p
for i in answer[::-1]:
    print(i)