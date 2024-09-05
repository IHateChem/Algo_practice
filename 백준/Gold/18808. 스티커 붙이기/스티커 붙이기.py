import sys
input = sys.stdin.readline
N, M, K = map(int,input().split())
stickers = []
answer = 0
for _ in range(K):
    R,C = map(int,input().split())
    sticker = [list(map(int,input().split())) for _ in range(R)]
    stickers.append(sticker)
papers = [[0]*M for _ in range(N)]
def canStick(x,y,sticker):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 1:
                if 0<=x+i<N and 0<=y+j<M:
                    if papers[x+i][y+j] == 1:
                        return False
                else:
                    return False
    return True
def stick(x,y,sticker):
    t = 0
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 1:
                t += 1
                papers[x+i][y+j] = 1  
    return t
def rotate(sticker):
    return list(zip(*sticker[::-1]))
for sticker in stickers:
    for _ in range(4):
        R,C = len(sticker),len(sticker[0])
        for i in range(N-R+1):
            for j in range(M-C+1):
                if canStick(i,j,sticker):
                    answer += stick(i,j,sticker)
                    break
            else:
                continue
            break
        else:
            sticker = rotate(sticker)
            continue
        break
print(answer)