import sys
input=sys.stdin.readline
N = int(input())
like = [[] for _ in range(N**2+1)]
classroom = [[0]*N for i in range(N)]
def satisfied(x,y, friends):
    ret = [0,0]
    if x > 0:
        if not classroom[x-1][y]: ret[1] += 1
        if classroom[x-1][y] in friends: ret[0] += 1
    if y > 0:
        if not classroom[x][y-1]: ret[1] += 1
        if classroom[x][y-1] in friends: ret[0] += 1
    if x < N-1:
        if not classroom[x+1][y]: ret[1] += 1
        if classroom[x+1][y] in friends: ret[0] += 1
    if y < N-1:
        if not classroom[x][y+1]: ret[1] += 1
        if classroom[x][y+1] in friends: ret[0] += 1
    return tuple(ret)
for _ in range(N**2):
    a = list(map(int, input().split()))
    like[a[0]] = set(a[1:])
    candidates = set()
    pos = (-1,-1)
    _max = (0,-1)
    for i in range(N):
        for j in range(N):
            if classroom[i][j]: continue
            score = satisfied(i,j, like[a[0]])
            if score > _max:
                pos = (i,j)
                _max = score
    classroom[pos[0]][pos[1]] = a[0]
answer = 0
scores = [0,1,10,100,1000]
for i in range(N):
    for j in range(N):
        answer += scores[satisfied(i,j, like[classroom[i][j]])[0]]
print(answer)