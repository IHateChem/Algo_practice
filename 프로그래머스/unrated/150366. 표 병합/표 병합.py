#DFS이용한 풀이
sheets = [["" for _ in range(51)] for __ in range(51)]
links = [[[] for _ in range(51)] for __ in range(51)]
def solution(commands):
    answer = []
    for command in commands:
        function(answer, *command.split())
    return answer
def function(answer, order, r, c, value = 0, value2 = 0):
    if order == "UPDATE":
        if value: _update(int(r),int(c),value)
        else: _change(r,c)
    elif order == "MERGE":
        _merge(*map(int, [r,c,value, value2]))
    elif order == "UNMERGE":
        _unmerge(int(r),int(c))
    elif order == "PRINT":
        _print(answer, int(r),int(c))
def _update(r, c, val):
    visited = set()
    stack = [(r,c)]
    while stack:
        u, v = stack.pop()
        if (u,v) in visited: continue
        visited.add((u, v))
        sheets[u][v] = val
        for x, y in links[u][v]:
            if not (x,y) in visited:
                stack.append((x,y))
    return visited
def _change(v1, v2):
    for i in range(1, 51):
        for j in range(1, 51):
            if sheets[i][j] == v1:
                sheets[i][j] = v2
def _merge(r1, c1, r2, c2):
    links[r1][c1].append((r2,c2))
    links[r2][c2].append((r1,c1))
    if sheets[r1][c1]:
        _update(r1,c1, sheets[r1][c1])
    else:
        _update(r2,c2, sheets[r2][c2])
def _unmerge(r, c):
    value = sheets[r][c]
    visited = _update(r, c, "")
    sheets[r][c] = value
    for u, v in visited:
        links[u][v] = []
def _print(answer, r, c):
    answer.append(sheets[r][c] if sheets[r][c] else "EMPTY")