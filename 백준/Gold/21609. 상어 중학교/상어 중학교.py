import sys
input = sys.stdin.readline
N, M =map(int, input().split())
MAP = [list(map(int,input().split())) for _ in range(N)] 

def findGroup():
    groups = []
    tot_visited = set()
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 0 or (i, j) in tot_visited or MAP[i][j] == -1 or MAP[i][j] == -2: continue
            size = 0
            rainbow = 0
            most_big_row = N
            most_big_column = N
            start_pos = (i,j)
            stack = [(i,j)]
            color = MAP[i][j]
            visited = set([(i,j)])
            while stack:
                t_i, t_j = stack.pop()
                size += 1
                if MAP[t_i][t_j] == 0: rainbow += 1
                else: tot_visited.add((t_i, t_j))
                if MAP[t_i][t_j]:
                    most_big_row = min(most_big_row, t_i)
                    most_big_column = min(most_big_column, t_j)
                for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
                    if not (0<=t_i + di <N and 0<=t_j+dj<N): continue
                    if (t_i+di,t_j+dj) in visited: continue
                    if MAP[t_i+di][t_j+dj] == 0 or MAP[t_i+di][t_j+dj] == color:
                        stack.append((t_i+di, t_j+dj))
                        visited.add((t_i+di, t_j+dj))
            groups.append((size, rainbow, most_big_row, most_big_column, start_pos, color))
    if not groups: return 0
    size, rainbow, most_big_row, most_big_column, start_pos, color = max(groups)
    if size == 1: return 0
    stack = [start_pos]
    visited = set([start_pos])
    while stack:
        t_i, t_j = stack.pop()
        MAP[t_i][t_j] = -2
        for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
            if not (0<=t_i + di <N and 0<=t_j+dj<N): continue
            if (t_i+di,t_j+dj) in visited: continue
            if MAP[t_i+di][t_j+dj] == 0 or MAP[t_i+di][t_j+dj] == color:
                stack.append((t_i+di, t_j+dj))
                visited.add((t_i+di, t_j+dj))
    return size ** 2
from collections import deque
def gravity():
    for j in range(N):
        s = N-1
        blacks = deque()
        for i in range(N-1, -1, -1):
            if MAP[i][j] == -1: blacks.append(i)
        blacks.append(-1)
        while blacks:
            puts = deque()
            e = blacks.popleft()
            for i in range(s, e, -1):
                if MAP[i][j] != -1 and MAP[i][j] != -2: puts.append(MAP[i][j])
            for i in range(s, e, -1):
                if MAP[i][j] == -1: continue
                if puts:
                    MAP[i][j] = puts.popleft()
                else:
                    MAP[i][j] = -2
            s = e
def rotateccw():
    new_MAP = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_MAP[N-1-i][j] = MAP[j][i]
    return new_MAP

answer = 0
while 1:
    size = findGroup()
    if not size: break
    answer += size
    gravity()
    MAP = rotateccw()
    gravity()
print(answer)