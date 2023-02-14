import sys
input = sys.stdin.readline
N,M,L,K=map(int,input().split())
stars = []
star_x = [];star_y = []
for _ in range(K):
    x ,y = map(int, input().split())
    star_x.append(x); star_y.append(y)
    stars.append((x,y))
star_x.sort();star_y.sort()
answer = 0
def get_candidates(x, y):
    xplus = x+L if x+L < N else N-1
    xminus = x-L if x-L > 0 else 0
    yplus = y+L if y+L < M else M-1
    yminus = y-L if y-L > 0 else 0
    return [((xplus-L, xplus), (yplus-L, yplus)), ((xplus-L, xplus), (yminus, yminus+L)), ((xminus, xminus+L), (yplus-L, yplus)),((xminus, xminus+L), (yminus, yminus+L))]
for x in star_x:
    for y in star_y:
        t = 0
        for _x, _y in stars:
            if x <= _x <= x+L and y <= _y <= y+L: t+= 1
        answer = max(t, answer)
print(K-answer)