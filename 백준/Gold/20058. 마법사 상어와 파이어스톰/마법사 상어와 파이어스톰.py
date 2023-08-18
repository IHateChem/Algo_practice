import sys
input = sys.stdin.readline
N,T = map(int, input().split())
MAP = []
for _ in range(2**N):
    MAP.append(list(map(int, input().split())))
def rotate(x,y,l, arr):
    n = 2**l	# 기존 행렬의 행의 길이
    new_arr = [[0] * n for _ in range(n)]
    for i in range(n):		# 기존 행렬의 행 이동
        for j in range(n):	# 기존 행렬의 열 이동
            new_arr[j][n - 1 - i] = arr[x+i][y+j]
    for i in range(n):
        for j in range(n):
            arr[x+i][y+j] = new_arr[i][j]
def melt(arr):
    N = len(arr)
    melts=[]
    for i in range(N):
        for j in range(N):
            s = 0
            if i > 0 and arr[i-1][j]: s+= 1
            if j>0 and arr[i][j-1]: s+=1
            if j+1<N and arr[i][j+1]: s+= 1
            if i+1<N and arr[i+1][j]:s += 1
            if s < 3 and arr[i][j]: melts.append((i,j))
    for i,j in melts:
        arr[i][j] -= 1
def dung_a_ri(arr):
    answer = 0
    N = len(arr)
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                stack = [(i,j)]
                t = 0
                arr[i][j] = 0
                while stack:
                    i,j = stack.pop()
                    t += 1
                    if i > 0 and arr[i-1][j]:
                        stack.append((i-1,j))
                        arr[i-1][j] = 0
                    if j>0 and arr[i][j-1]:
                        stack.append((i,j-1))
                        arr[i][j-1] = 0
                    if j+1<N and arr[i][j+1]:
                        stack.append((i,j+1))
                        arr[i][j+1] = 0
                    if i+1<N and arr[i+1][j]:
                        stack.append((i+1,j))
                        arr[i+1][j] = 0
                answer = max(answer, t)
    return answer
for l in map(int,input().split()):
    if l:
        pnt = 0
        while l+pnt <= 2**N:
            lpnt = 0
            while l+lpnt <= 2**N:
                rotate(lpnt, pnt, l, MAP)
                lpnt += 2**l
            pnt  += 2**l
    melt(MAP)   
s = 0
for i in MAP: s+= sum(i)
print(s)
print(dung_a_ri(MAP))