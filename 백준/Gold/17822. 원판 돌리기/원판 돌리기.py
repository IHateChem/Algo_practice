import sys
input = sys.stdin.readline
N,M,T = map(int,input().split())
circles = [list(map(int,input().split())) for _ in range(N)]
index = [0]*N
dir = [-1, 1]
def rotate(x, d, k):
    for i in range(1, N):
        if i*x > N: break
        index[i*x-1] = (index[i*x-1] +dir[d]*k) % M
    pass
def findEqual():
    t = [[] for _ in range(N)]
    t2 = [[] for _ in range(N)]
    flag = True
    for i in range(N):
        for j in range(M):
            if circles[i][j]!="x" and circles[i][j] == circles[i][(j+1)%M]:
                t[i].extend([j, (j+1)%M])
        if i < N-1:
            for j in range(M):
                if circles[i][(index[i]+j)%M]!="x" and circles[i][(index[i]+j)%M] == circles[i+1][(index[i+1]+j)%M]: t2[i].append(j)
        if t[i] or t2[i]: flag = False
    if flag:
        findMean()
    else:
        for i in range(N):
            for j in t[i]:
                circles[i][j] = "x"
            for j in t2[i]:
                circles[i][(index[i]+j)%M] = "x"
                circles[i+1][(index[i+1]+j)%M] = "x"

def findMean():
    tot = 0
    n = 0
    for i in range(N):
        for j in range(M):
            if circles[i][j] != "x":
                tot += circles[i][j]
                n += 1
    if not n: return
    avg = tot / n
    for i in range(N):
        for j in range(M):
            if circles[i][j] != "x":
                if circles[i][j] > avg:
                    circles[i][j] -= 1
                elif circles[i][j] < avg:
                    circles[i][j] += 1

def sum():
    tot = 0
    for i in range(N):
        for j in range(M):
            if circles[i][j] != "x":
                tot += circles[i][j]
    return tot
    

for x, d, k in [map(int,input().split()) for _ in range(T)]:
    rotate(x, d, k)
    findEqual()
print(sum())