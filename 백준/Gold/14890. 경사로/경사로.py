import sys
input=sys.stdin.readline
N,L=map(int,input().split())
MAP=[list(map(int,input().split())) for _ in range(N)]
def ramprow():
    ans = 0
    for i in range(N):
        p = MAP[i][0]
        seq = 1
        flag = False
        for j in range(1, N):
            if MAP[i][j] == p:
                seq += 1
                if flag and seq >= L: 
                    p = MAP[i][j]
                    seq = 0
                    flag = False
            elif abs(MAP[i][j] - p) > 1: break
            elif MAP[i][j] - p == 1:
                if seq >= L:
                    p = MAP[i][j]
                    seq = 1
                else: break
            else:
                if flag: break
                flag = True
                p = MAP[i][j]
                seq = 1
                if flag and seq >= L: 
                    p = MAP[i][j]
                    seq = 0
                    flag = False
        else:
            if flag:
                if seq < L: continue
            ans += 1
    return ans
def rampCol():
    ans = 0
    for j in range(N):
        p = MAP[0][j]
        seq = 1
        flag = False
        for i in range(1, N):
            if MAP[i][j] == p:
                seq += 1
                if flag and seq >= L: 
                    p = MAP[i][j]
                    seq = 0
                    flag = False
            elif abs(MAP[i][j] - p) > 1: break
            elif MAP[i][j] - p == 1:
                if seq >= L:
                    p = MAP[i][j]
                    seq = 1
                else: break
            else:
                if flag: break
                flag = True
                p = MAP[i][j]
                seq = 1
                if flag and seq >= L: 
                    p = MAP[i][j]
                    seq = 0
                    flag = False
        else:
            if flag:
                if seq < L: continue
            ans += 1
    return ans
print(rampCol() + ramprow())