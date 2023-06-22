import sys
input = sys.stdin.readline
R,C = map(int,input().split())
MAP = [list(input().strip()) for _ in range(R)]
directions = [(1,0), (-1,0),(0,1),(0,-1)]
waters = set()
hedgehogs = set()
beavors = set()
history = set()
for r in range(R):
    for c in range(C):
        if MAP[r][c] == "D": beavors.add((r,c))
        elif MAP[r][c] == "*": waters.add((r,c))
        elif MAP[r][c] == "S": hedgehogs.add((r,c))

def canExpand(r,c,t):
    if t: return MAP[r][c] != "X" and MAP[r][c] != "D" and MAP[r][c] != "*"
    else: return MAP[r][c] != "X" and MAP[r][c] != "*"
def Expansion(r, c, tp, retset): #tp는 확장 타입 -> 1이면 물 0이면 고슴도치
    for dr, dc in directions:
        if 0<=r+dr<R and 0<=c+dc<C and canExpand(r+dr,c+dc,tp):
            retset.add((r+dr, c+dc))
            if tp: MAP[r+dr][c+dc] = "*"
cnt  = 0
while hedgehogs:
    cnt += 1
    nextWater = set()
    for r, c in waters:
        Expansion(r,c,1, nextWater)
    waters = nextWater
    nextHegehogs = set()
    for r, c in hedgehogs:
        if(r,c)in history: continue
        history.add((r,c))
        Expansion(r,c,0, nextHegehogs)
    hedgehogs = nextHegehogs
    if hedgehogs&beavors:
        print(cnt)
        exit(0)
print("KAKTUS")