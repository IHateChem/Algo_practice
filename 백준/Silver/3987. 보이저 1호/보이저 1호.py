import sys
INF=1000000
N,M=map(int, input().split())
MAP=[list(input().strip()) for _ in range(N)]
R,C=map(int,input().split())
R-=1;C-=1
directions={"U":(-1,0),"R": (0,1),"D":(1,0),"L":(0,-1)}
rotate={"\\":lambda x,y: (y,x), "/":lambda x,y: (-y,-x), ".":lambda x,y:0, "C":lambda x,y:0}
answer=(0,"")
for direction in directions:
    dr, dc = directions[direction]
    time=0
    r,c=R,C
    while time < INF and 0<=r<N and 0<=c<M and MAP[r][c] != "C":
        if rotate[MAP[r][c]](dr,dc):
            dr, dc = rotate[MAP[r][c]](dr,dc)
        r += dr
        c += dc
        time += 1
    answer=max(answer, (time,direction))
if answer[0] == INF: print(answer[1]);print("Voyager")
else: print(answer[1]); print(answer[0])

