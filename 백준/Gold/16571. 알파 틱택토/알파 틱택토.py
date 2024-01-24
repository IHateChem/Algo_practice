import sys
from collections import defaultdict as dd
input = sys.stdin.readline
MAP = [list(map(int,input().split()))for _ in range(3)]
turn = 0
for i in range(3):
    for j in range(3):
        if not MAP[i][j]: continue
        if MAP[i][j] == 1: turn += 1
        else: turn -= 1
turn %= 2
def check(turn):
    t = turn+1
    e = t % 2 + 1
    zeros = sum([0 in MAP[i] for i in range(3)])
    if(MAP[0][0]==MAP[1][1]==MAP[2][2]==t): return "W"
    if(MAP[0][2]==MAP[1][1]==MAP[2][0]==t): return "W"
    if(MAP[0][0]==MAP[1][1]==MAP[2][2]==e): return "L"
    if(MAP[0][2]==MAP[1][1]==MAP[2][0]==e): return "L"
    for i in range(3):
        if(MAP[i][0]==MAP[i][1]==MAP[i][2]==t): return "W"
        if(MAP[0][i]==MAP[1][i]==MAP[2][i]==t): return "W"
        if(MAP[i][0]==MAP[i][1]==MAP[i][2]==e): return "L"
        if(MAP[0][i]==MAP[1][i]==MAP[2][i]==e): return "L"
    if zeros: return "N"
    return "D"
def do(turn):
    t = turn + 1
    resultSet = set()
    for i in range(3):
        for j in range(3):
            if MAP[i][j]: continue
            MAP[i][j] = t
            c = check(turn)
            if c == "W": resultSet.add("W")
            elif c == "L": resultSet.add("L")
            elif c == "D": resultSet.add("D")
            else: resultSet.add(do((turn+1)%2))
            MAP[i][j] = 0
            if "W" in resultSet: return "L"
    if "D" in resultSet: return "D"
    return "W"
change = {"W":"L", "L": "W", "D": "D"}
print(change[do(turn)])