import sys
input= sys.stdin.readline
N,M,H = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    students[i].append(0)
dp = [[0]*N for _ in range(H+1)]
for s in students[0]:
    dp[s][0] = 1
for i in range(1, N):
    student = students[i]
    for j in range(H+1):
        for s in student:
            if j+s < H+1 and dp[j][i-1]: dp[j+s][i] += dp[j][i-1]
print(dp[-1][-1]%10007)