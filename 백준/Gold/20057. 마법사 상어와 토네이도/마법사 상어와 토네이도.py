import sys
input = sys.stdin.readline
N = int(input())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))
dir = [(0,-1), (1,0),(0,1), (-1,0)]
def get_flatter(dir):
    x = dir[0]
    y = dir[1]
    if y:
        flatter = [
            ((1,0),0.01), ((-1,0),0.01),
            ((1,y),0.07), ((-1,y),0.07),((2,y),0.02), ((-2,y),0.02),
            ((1,2*y),0.1), ((-1,2*y),0.1),
            ((0,3*y), 0.05)
        ]
    else:
        flatter = [
            ((0,1),0.01), ((0,-1),0.01),
            ((x,1),0.07), ((x,-1),0.07),((x,2),0.02), ((x,-2),0.02),
            ((2*x,1),0.1), ((2*x,-1),0.1),
            ((3*x,0), 0.05)
        ]
    return flatter
answer = 0
distance = 0
d = 0
cnt = 0
x = N//2; y= N//2
while x or y:
    if cnt % 2==0: distance += 1
    for i in range(distance):
        tot = 0
        sand = MAP[x+dir[d][0]][y+dir[d][1]]
        for (dx, dy), p in get_flatter(dir[d]):
            if x+dx < 0 or x+dx >= N or dy +y< 0 or y+dy >=N:
                answer += int(sand * p)
                tot += int(sand * p)
            else:
                MAP[x+dx][y+dy] += int(sand*p)
                tot += int(sand*p)
        dx = 2*dir[d][0];dy =2*dir[d][1]
        if x+dx < 0 or x+dx >= N or dy +y< 0 or y+dy >=N:
            answer += sand - tot
        else:
            MAP[x+dx][y+dy] += sand - tot
        x += dir[d][0]
        y += dir[d][1]
        if not (x or y): break
    d = (d+1)%4
    cnt += 1
print(answer)