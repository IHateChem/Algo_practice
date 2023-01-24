import sys
from collections import defaultdict as dd
input = sys.stdin.readline
R, C, M = map(int, input().split())
dpos = {1:(-1, 0), 2:(1,0),3:(0,1),4:(0,-1)}
limit = {1:(0, 1, R*2-2), 2:(0,R, R*2-2),3:(1,C, C*2-2),4:(1,1, C*2-2)}
MAP = [[-1 for _ in range(C+1)] for i in range(R+1)]
next = {1:2, 2:1, 3:4, 4:3}
sharks = [] #(위치, 속력, 이동방향, 크기, 생사여부)
catched = 0
def catch(i):
    global catched
    for k in range(1, R+1):
        if MAP[k][i] != -1:
            id = MAP[k][i]
            sharks[id][-1] = 0
            catched += sharks[id][3]
            break
def move():
    ret_sharks = []
    new_MAP = [[-1 for _ in range(C+1)] for i in range(R+1)]
    id = -1
    isalive = dd(int)
    for pos, s, d, z, f in sharks:
        id += 1
        if not f: continue
        for i in range(s):
            if pos[limit[d][0]] == limit[d][1]:
                d = next[d]
            pos[0] += dpos[d][0]
            pos[1] += dpos[d][1]
        sharks[id][2] = d
        if new_MAP[pos[0]][pos[1]] != -1:
            if sharks[new_MAP[pos[0]][pos[1]]][3] > z: continue
            isalive[new_MAP[pos[0]][pos[1]]] = 0
        new_MAP[pos[0]][pos[1]] = id
        isalive[id] = 1
    id = -1
    for pos, s, d, z, f in sharks:
        id += 1
        if isalive[id]: ret_sharks.append([pos, s, d, z, f])
    id = -1
    for pos, s, d, z, f in ret_sharks:
        id += 1
        new_MAP[pos[0]][pos[1]] = id
    return ret_sharks, new_MAP
for _ in range(M):
    r,c,s,d,z, = map(int, input().split())
    sharks.append([[r,c], s%limit[d][2], d, z, 1])
    MAP[r][c] = _
for i in range(1, C+1):
    catch(i)
    sharks, MAP = move()
print(catched)