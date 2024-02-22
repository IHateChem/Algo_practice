MAP = [list(input().strip()) for _ in range(8)]
MAP[-1][0] = 1
def check():
    if MAP[0][-1] == 1: return False
    for i in range(8):
        for j in range(8):
            if MAP[i][j] == 1: return True
    return False
outbound = lambda x, y: x < 0 or x > 7 or y < 0 or y > 7
while check():
    newMAP = [["." for i in range(8)]for j in range(8)]
    for i in range(8):
        for j in range(8):
            if MAP[i][j] == "#" and i < 7:
                newMAP[i+1][j] = "#"
            if MAP[i][j] != 1: continue
            for di, dj in ((1,0), (0,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)):
                if outbound(i+di, j+dj) or newMAP[i+di][j+dj] != "." or MAP[i+di][j+dj] == "#": continue
                newMAP[i+di][j+dj] = 1
    MAP = newMAP
print(1 if MAP[0][-1] == 1 else 0)