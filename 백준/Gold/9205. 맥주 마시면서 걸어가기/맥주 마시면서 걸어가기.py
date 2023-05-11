import sys
input = sys.stdin.readline
t = int(input())
def dfs(u):
    x, y = convinience[u]
    if get_dist(x,y, fest_x, fest_y) <= 1000:
        return 1
    for v in range(1, N+1):
        if (not visited[v]) and get_dist(x,y, *convinience[v]) <= 1000:
            visited[v] = 1
            if dfs(v): return 1
    return 0
get_dist = lambda x, y, r, s: abs(x- r) + abs(y- s)
for i in range(t):
    N = int(input())
    x, y = map(int, input().split())
    convinience = [(x,y)]
    for _ in range(N):
        convinience.append(tuple(map(int, input().split())))
    #convinience = [tuple(map(int, input().split()) for i in range(N))] #  [(x,y)]+
    fest_x, fest_y = map(int, input().split())
    visited = [0] * (N+1)
    visited[0] = 1
    if dfs(0): print("happy")
    else: print("sad")