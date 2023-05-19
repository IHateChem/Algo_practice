import sys
from itertools import combinations as C
input = sys.stdin.readline
results = [list(map(int, input().split())) for _ in range(4)]
def simulWL(i):
    defeats = set(); a = 0
    for j in range(6): a += result[j*3+2]
    if a == 0: return 1
    if i == 6: return 0
    if not result[3*i]: return simulWL(i+1)
    for j in range(6):
        if j != i and result[j*3+2] and not visited[i][j]: defeats.add(j)
    for possible in C(defeats, result[i*3]):
        for p in possible:
            visited[i][p] = 1
            visited[p][i] = 1
            result[p*3+2] -= 1
        if simulWL(i+1): return 1
        for p in possible:
            result[p*3+2] += 1
            visited[i][p] = 0
            visited[p][i] = 0
    return 0
def simulDraw(i):
    draws = set(); a = 0
    for j in range(6): a += result[j*3+1]
    if a == 0: return 1
    if i == 6: return 0
    if not result[3*i+1]: return simulWL(i+1)
    for j in range(6):
        if j != i and result[j*3+1] and not visited[i][j]: draws.add(j)
    for possible in C(draws, result[i*3+1]):
        for p in possible:
            visited[i][p] = 1
            visited[p][i] = 1
            result[p*3+1] -= 1
        if simulDraw(i+1): return 1
        for p in possible:
            result[p*3+1] += 1
            visited[i][p] = 0
            visited[p][i] = 0
    return 0
for result in results:
    visited = [[0]*6 for _ in range(6)]
    if sum(result) != 30:
        print(0, end = " ")
        continue
    print(simulWL(0)*simulDraw(0), end = " ")