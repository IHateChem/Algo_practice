import sys
import heapq
input = sys.stdin.readline
T = int(input())
def checkdu(MAP, i, W):
    if MAP[0][i]+MAP[1][i] <= W: return 1
    return 2
def checklr(MAP, i, W, j):
    if MAP[j][i]+MAP[j][i-1] <= W: return 1
    return 2


for _ in range(T):
    N, W = map(int, input().split())
    MAP = []
    for i in range(2):
        MAP.append(list(map(int, input().split())))
    a = [0] * N
    b = [0] * N
    c = [0] * N
    b[0] = 1; c[0] = 1
    for i in range(1, N):
        a[i] = min(a[i-1] + checkdu(MAP, i-1, W), b[i-1]+1, c[i-1]+1, a[i-2]+checklr(MAP, i-1, W, 0)+checklr(MAP, i-1, W, 1))
        b[i] = min(c[i-1] + checklr(MAP, i, W, 0), a[i]+1)
        c[i] = min(b[i-1] + checklr(MAP, i, W, 1), a[i]+1)
    answer = min(a[N-1] + checkdu(MAP, N-1, W), b[N-1]+1, c[N-1]+1, a[N-2]+checklr(MAP, N-1, W, 0)+checklr(MAP, N-1, W, 1))
    if N >= 3:
        if MAP[0][0] + MAP[0][-1] <= W and MAP[1][0] + MAP[1][-1] <= W:
            a = [0] * N
            b = [0] * N
            c = [0] * N
            a[0] = 2; b[0] = 3; c[0] = 3
            a[1] = 2; b[1] = 3; c[1] = 3
            for i in range(2, N-1):
                a[i] = min(a[i-1] + checkdu(MAP, i-1, W), b[i-1]+1, c[i-1]+1, a[i-2]+checklr(MAP, i-1, W, 0)+checklr(MAP, i-1, W, 1))
                b[i] = min(c[i-1] + checklr(MAP, i, W, 0), a[i]+1)
                c[i] = min(b[i-1] + checklr(MAP, i, W, 1), a[i]+1)
            answer = min(answer, a[N-2] + checkdu(MAP, N-2, W), b[N-2]+1, c[N-2]+1, a[N-3]+checklr(MAP, N-2, W, 0)+checklr(MAP, N-2, W, 1))
        if MAP[0][0] + MAP[0][-1] <= W:
            a = [0] * N
            b = [0] * N
            c = [0] * N
            a[0] = 1; b[0] = 1; c[0] = 1
            a[1] = 2; b[1] = 3; c[1] = 1 + checklr(MAP, 1, W, 1)
            for i in range(2, N-1):
                a[i] = min(a[i-1] + checkdu(MAP, i-1, W), b[i-1]+1, c[i-1]+1, a[i-2]+checklr(MAP, i-1, W, 0)+checklr(MAP, i-1, W, 1))
                b[i] = min(c[i-1] + checklr(MAP, i, W, 0), a[i]+1)
                c[i] = min(b[i-1] + checklr(MAP, i, W, 1), a[i]+1)
            answer = min(answer, a[N-2] + checkdu(MAP, N-2, W) + 1, b[N-2]+checklr(MAP, N-1, W, 1), c[N-2]+2)
        if MAP[1][0] + MAP[1][-1] <= W:
            a = [0] * N
            b = [0] * N
            c = [0] * N
            a[0] = 1; b[0] = 1; c[0] = 1
            a[1] = 2; b[1] = 1 + checklr(MAP, 1, W, 0); c[1] = 3
            for i in range(2, N-1):
                a[i] = min(a[i-1] + checkdu(MAP, i-1, W), b[i-1]+1, c[i-1]+1, a[i-2]+checklr(MAP, i-1, W, 0)+checklr(MAP, i-1, W, 1))
                b[i] = min(c[i-1] + checklr(MAP, i, W, 0), a[i]+1)
                c[i] = min(b[i-1] + checklr(MAP, i, W, 1), a[i]+1)
            answer = min(answer, a[N-2] + checkdu(MAP, N-2, W) + 1, c[N-2]+checklr(MAP, N-1, W, 0), b[N-2]+2)
    print(answer)