from collections import deque, defaultdict
import sys
input = sys.stdin.readline

N = int(input())  # 완제품 번호 = N
M = int(input())  # 관계 수

indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
dp = [defaultdict(int) for _ in range(N + 1)]  # 각 부품별 필요한 기본 부품 수

for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[Y].append((X, K))  # Y -> X, 즉 X 만들기 위해 Y가 필요
    indegree[X] += 1

queue = deque()

# 기본 부품: indegree가 0인 부품들
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
        dp[i][i] = 1  # 기본 부품은 자기 자신 1개만 필요

while queue:
    current = queue.popleft()

    for next_part, count in graph[current]:
        for key in dp[current]:  # current의 모든 기본 부품들에 대해
            dp[next_part][key] += dp[current][key] * count
        indegree[next_part] -= 1
        if indegree[next_part] == 0:
            queue.append(next_part)

# 출력: 완제품 N을 만들기 위해 필요한 기본 부품
result = dp[N]
for part in sorted(result):
    print(part, result[part])
