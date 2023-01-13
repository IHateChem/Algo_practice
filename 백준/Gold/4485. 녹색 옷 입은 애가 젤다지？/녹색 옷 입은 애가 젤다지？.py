import sys
import heapq
input = sys.stdin.readline
dpos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
k = 1
while 1:
    n = int(input())
    if n == 0: break
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    stack = [(graph[0][0], 0 , 0)]
    visited = [[0 for _ in range(n)] for i in range(n)]
    visited[0][0] = 1
    while stack:
        w, x, y = heapq.heappop(stack)
        for dx, dy in dpos:
            if dx + x >= 0 and dx + x < n:
                if not visited[x+dx][y]:
                    heapq.heappush(stack, (w+graph[x+dx][y], x+dx, y))
                    if (x+dx, y) == (n-1, n-1):
                        print(f"Problem {k}: {w+graph[x+dx][y]}")
                        stack = []
                        break
                    visited[x+dx][y] = 1
            if dy + y >= 0 and dy + y < n:
                if not visited[x][y+dy]:
                    heapq.heappush(stack, (w+graph[x][y+dy], x, y+dy))
                    if (x, y+dy) == (n-1, n-1):
                        print(f"Problem {k}: {w+graph[x][y+dy]}")
                        stack = []
                        break
                    visited[x][y+dy] = 1
    k +=1