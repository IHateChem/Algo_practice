import sys
input = sys.stdin.readline
n, m = map(int,input().split())
MAP = []
visited = [[0]*m for _ in range(n)]
group = [[-1]*m for _ in range(n)]
value = {}
idx = 0
dir = [(1,0), (-1,0), (0,1), (0,-1)]
for _ in range(n):
    MAP.append(input().strip())     
def dfs(x, y, val, idx):
    stack = [(x,y)]
    visited[x][y] = 1
    while stack:
        val += 1
        x, y = stack.pop()
        group[x][y] = idx
        for dx, dy in dir:
            if 0<= x+dx < n and 0<=y+dy<m:
                if visited[x+dx][y+dy] or MAP[x+dx][y+dy] == "1": continue
                visited[x+dx][y+dy] = 1
                stack.append((x+dx,y+dy))
    return val
for i in range(n):
    for j in range(m):
        if MAP[i][j] == "1" or visited[i][j]: continue
        size = dfs(i, j, 0, idx)
        value[idx] = size
        idx += 1
answer = []
for i in range(n):
    line = ""
    for j in range(m):
        t = 0
        history = set()
        if MAP[i][j] == "1":
            for dx, dy in dir:
                if 0<= i+dx < n and 0<=j+dy<m and MAP[i+dx][j+dy] == "0":
                    if group[i+dx][j+dy] in history: continue
                    t+=value[group[i+dx][j+dy]]
                    history.add(group[i+dx][j+dy])
        else:
            t = -1     
        line += str((t+1)%10)
    answer.append(line)
print("\n".join(answer))