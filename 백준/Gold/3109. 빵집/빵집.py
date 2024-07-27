import sys
input = sys.stdin.readline
R, C = map(int,input().split())
MAP = [list(input().strip()) for _ in range(R)]
inbound = lambda r,c : 0<=r<R and 0<=c<C
answer = 0
visited = set()
def calc(r, c, route):
    if (r,c) in visited: return 0
    visited.add((r,c))
    if c == C-1 or \
        (inbound(r-1,c+1) and MAP[r-1][c+1] == "." and calc(r-1, c+1, route)) or \
        (inbound(r, c+1) and MAP[r][c+1] == "." and calc(r, c+1, route)) or \
        (inbound(r+1, c+1) and MAP[r+1][c+1] == "." and calc(r+1,c+1, route)):
        route.append((r,c))
        return 1
    else:
        return 0
for i in range(R):
    route = []
    calc(i, 0, route)
    for r,c in route:
        MAP[r][c] = "o"
    if route: answer += 1
print(answer)