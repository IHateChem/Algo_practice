import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
N , M = map(int, input().split())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))
dp = [[-1]*M for _ in range(N)]
dp[0][0] = 1
stack = [(0, 0)]
def dpg(a, b):
    if dp[a][b] != -1: return dp[a][b]
    for dx, dy in [(-1, 0), (0, -1), (1,0), (0, 1)]:
        if dx + a >= 0  and dx + a < N and dy + b >= 0 and dy+ b < M:
            if MAP[a][b] < MAP[dx+a][dy+b]:
                if dp[a][b] == -1: dp[a][b] = dpg(dx+a, dy+b)
                else: dp[a][b] += dpg(dx+a, dy+b)
    return dp[a][b] if dp[a][b] != -1 else 0
dpg(N-1, M-1)
print(dp[-1][-1] if dp[-1][-1] != -1 else 0)