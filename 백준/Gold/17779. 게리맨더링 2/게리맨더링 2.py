import sys
input = sys.stdin.readline
N=int(input())
MAP=[list(map(int,input().split())) for _ in range(N)]
answer= 1000000000000
for d1 in range(1,N):
    for d2 in range(1,N):
        for x in range(N-d1-d2):
            for y in range(d1,N-d2):
                sections=[0]*5
                for r in range(N):
                    for c in range(N):
                        dx,dy = r-x,c-y
                        miny=-dx;maxy=dx
                        if d1<=dx<=d1+d2: miny=dx-2*d1
                        if d2<=dx<=d1+d2: maxy=d2-(dx-d2)
                        if 0<=dx<=d1+d2 and miny<=dy<=maxy: sections[4] += MAP[r][c]
                        elif r<x+d1 and c <= y: sections[0] += MAP[r][c]
                        elif r<=x+d2 and y<c: sections[1] += MAP[r][c]
                        elif r>= x+d1 and c<y-d1+d2: sections[2] += MAP[r][c]
                        elif r>x+d2 and y-d1+d2<=c: sections[3] += MAP[r][c]
                answer=min(answer, max(sections)-min(sections))
print(answer)