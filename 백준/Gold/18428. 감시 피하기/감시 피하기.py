from itertools import combinations as C
import sys
input = sys.stdin.readline
N = int(input())
MAP = []
places = []
teachers = []
def up(x, y, o):
    for dx in range(1, x+1):
        if (x-dx, y) in o: return False
        if MAP[x-dx][y] == "S": return True
    return False
def down(x, y, o):
    for dx in range(1, N-x):
        if (x+dx, y) in o: return False
        if MAP[x+dx][y] == "S": return True
    return False
def left(x, y, o):
    for dy in range(1, y+1):
        if (x, y-dy) in o: return False
        if MAP[x][y-dy] == "S": return True
    return False
def right(x, y, o):
    for dy in range(1, N-y):
        if (x, y+dy) in o: return False
        if MAP[x][y+dy] == "S": return True
    return False
def check(obstacles):
    for x, y in teachers:
        if up(x, y, obstacles): return False
        if down(x, y, obstacles): return False
        if left(x, y, obstacles): return False
        if right(x, y, obstacles): return False
    return True
for _ in range(N):
    MAP.append(list(input().strip().split()))
    for i, w in enumerate(MAP[-1]):
        if w == "X": places.append((_, i))
        if w == "T": teachers.append((_, i))
for obstacles in C(places, 3):
    if check(obstacles):
        print("YES")
        break
else: print("NO")