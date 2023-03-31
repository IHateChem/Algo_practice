import sys
from collections import defaultdict as dd
import math
input = sys.stdin.readline
N, K = map(int, input().split())
bowl = [[0]*N for _ in " "*N]
def putFish2minBowl(bowl):
    mins = []
    _min = 100000
    for i, b in enumerate(bowl[0]):
        if _min > b:
            mins = [i]
            _min = b
        elif _min == b:
            mins.append(i)
    for i in mins:
        bowl[0][i] += 1
def leftmost2right(bowl):
    bowl[1][1] = bowl[0][0]
    bowl[0][0] = 0
def WingardiumLeviosa1(bowl):
    end = -1
    start = -1
    for i in range(N-1,0,-1):
        for j in range(N):
            if bowl[j][i] == 0: break
        if j > 1:
            end = i
            height = j
            break
    if height > N - end - 1:
        return 
    for i in range(N):
        for j in range(N):
            if bowl[j][i] == 0: break
        if j > 1:
            start = i
            break
    index = 0
    for i in range(end, start-1, -1):
        for j in range(height):
            bowl[index+1][end+1+j] = bowl[j][i]
            bowl[j][i]= 0
        index += 1
    WingardiumLeviosa1(bowl)
def regulateFish(bowl):
    for i in range(N):
        if bowl[0][i] != 0: break
    regulate_where = dd(int)
    for j in range(i, N):
        for k in range(N):
            if bowl[k][j] == 0: break
            if j> 0 and bowl[k][j-1] != 0 and abs(bowl[k][j] - bowl[k][j-1]) >= 5:
                gap = abs(bowl[k][j] - bowl[k][j-1]) //5
                sign = -1 if bowl[k][j] < bowl[k][j-1] else 1
                regulate_where[(k, j-1)] += gap * sign
                regulate_where[(k, j)] += gap * sign*-1
            if k+1 < N and bowl[k+1][j] != 0 and abs(bowl[k+1][j] - bowl[k][j]) >= 5:
                gap = abs(bowl[k+1][j] - bowl[k][j])//5
                sign = -1 if bowl[k+1][j] > bowl[k][j] else 1
                regulate_where[(k+1, j)] += gap * sign 
                regulate_where[(k, j)] += gap * sign * -1
    for k, v in regulate_where.items():
        i ,j = k
        bowl[i][j] += v
    return
def rearrange(bowl):
    for start in range(N):
        if bowl[1][start]: break
    for end in range(N-1, -1, -1):
        if bowl[1][end]: break
    index = 0
    for i in range(start, end+1):
        for j in range(N):
            if not bowl[j][i]: break
            bowl[0][index] = bowl[j][i]
            bowl[j][i] = 0
            index += 1
def WingardiumLeviosa2(bowl):
    for i in range(N//2):
        bowl[1][N-1-i] = bowl[0][i]
        bowl[0][i] = 0
    for i in range(N//4):
        bowl[3][N-1-i] = bowl[0][N//2+i]
        bowl[2][N-1-i] = bowl[1][N//2+i]
        bowl[0][N//2+i] = 0
        bowl[1][N//2+i] = 0
def checkbowl(bowl):
    _min = 100000
    _max = -1
    for i in range(N):
        if bowl[0][i] < _min:
            _min =  bowl[0][i]
        if bowl[0][i] > _max:
            _max =  bowl[0][i]
    return _max - _min
for i, _ in enumerate(map(int, input().split())):
    bowl[0][i] = _
answer = 0
while checkbowl(bowl) > K:
    putFish2minBowl(bowl)
    leftmost2right(bowl)
    WingardiumLeviosa1(bowl)
    regulateFish(bowl)
    rearrange(bowl)
    WingardiumLeviosa2(bowl)
    regulateFish(bowl)
    rearrange(bowl)
    answer += 1
print(answer)