'''
103000509
002109400
000704000
300502006
060000050
700803004
000401000
009205800
804000107
'''
import sys
import copy
input = sys.stdin.readline
sdk = []
for _ in range(9):
    sdk.append([int(i) for i in input().strip()])
possible = copy.deepcopy(sdk)
blank = []
for i in range(9):
    t = set(range(1, 10))
    for m in range(9):
        if sdk[i][m]:
            t.remove(sdk[i][m])
        else:
            blank.append((i, m))
    for m in range(9):
        if not sdk[i][m]:
            possible[i][m] = copy.deepcopy(t)

for i in range(9):
    t = set(range(1, 10))
    for m in range(9):
        if sdk[m][i]:
            t.remove(sdk[m][i])
    for m in range(9):
        if  type(possible[m][i]) == set:
            possible[m][i] = possible[m][i] & t
for i in range(3):
    for m in range(3):
        t = set(range(1, 10))
        for ii in range(3):
            for mm in range(3):
                if sdk[i*3+ii][m*3+mm]:
                    t.remove(sdk[i*3+ii][m*3+mm])
        for ii in range(3):
            for mm in range(3):
                if type(possible[i*3+ii][m*3+mm]) == set:
                    possible[i*3+ii][m*3+mm] = possible[i*3+ii][m*3+mm] & t
def check(i, j, a):
    for m in range(9):
        if sdk[i][m]:
            if sdk[i][m] == a:
                return False
    for m in range(9):
        if sdk[m][j]:
            if sdk[m][j] == a:
                return False
    for m in range(3):
        for n in range(3):
            if sdk[i//3 *3 + m][j//3 *3+ n]:
                if sdk[i//3*3 + m][j//3*3 + n]== a:
                    return False
    return True

def dfa(id):
    if id == len(blank):
        for i in range(9):
            print("".join(map(str, sdk[i])))
        exit(0)
    x = blank[id][0]
    y = blank[id][1]
    for i in possible[x][y]:
        if check(x, y, i):
            sdk[x][y] = i
            dfa(id+1)
            sdk[x][y] = 0
dfa(0)