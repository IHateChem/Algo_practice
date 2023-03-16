import sys
from collections import defaultdict as dd
input = sys.stdin.readline
R, C = map(int, input().split())
MAP = []
J_pos = []
crazies = []
broken = set()
for _ in range(R):
    MAP.append(input().strip())
    for j, m in enumerate(MAP[-1]):
        if m == "I": J_pos = [_, j]
        elif m == "R": crazies.append([_, j])
def getdist(p1, p2): return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
def moveCrazy():
    for c, c_pos in enumerate(crazies):
        if c in broken: continue
        _min = 255
        _dir = 0
        for i in range(1, 10):
            t_pos = [c_pos[_] + dir[i][_] for _ in range(2)]
            if _min > getdist(J_pos, t_pos):
                _min = getdist(J_pos, t_pos)
                _dir = i
        for i in range(2): c_pos[i] += dir[_dir][i]
        if c_pos == J_pos: return True
    bomb()
    return False
def bomb():
    history = dd(int)
    for c, c_pos in enumerate(crazies):
        if c in broken: continue
        if history[tuple(c_pos)]:
            broken.add(c)
            broken.add(history[tuple(c_pos)]-1)
        else:
            history[tuple(c_pos)] = c + 1
dir = [(),(1,-1), (1,0), (1,1), (0, -1), (0,0), (0,1), (-1, -1), (-1, 0), (-1, 1)]
strings = input().strip()
for n, s in enumerate(strings):
    for i in range(2): J_pos[i] += dir[int(s)][i]
    for c, c_pos in enumerate(crazies):
        if c in broken: continue
        if c_pos == J_pos: break
    else:
        if moveCrazy(): break
        continue
    break
else:
    for i in range(R):
        t = ""
        for j in range(C):
            if [i,j] == J_pos:
                t += "I"
            else:
                for c, c_pos in enumerate(crazies):
                    if c in broken: continue
                    if [i,j] == c_pos:
                        t += "R"
                        break
                else:
                    t += "."
        print(t)
    exit()
print("kraj", n+1)