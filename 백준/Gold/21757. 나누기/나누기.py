import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
preSum = [0] * N
for i in range(N):
    preSum[i] = preSum[i-1] + numbers[i]
n = sum(numbers)//4
dp = [[0]* 4 for _ in range(N)]
if sum(numbers) % 4 != 0:
    print(0)
    exit(0)
if n == 0:
    zeros = preSum.count(0) - 1
    print(zeros*(zeros-1)*(zeros-2)//6)
    exit(0)
for i in range(N):
    for j in range(4):
        if preSum[i] % n == 0 and preSum[i] // n == j + 1:
            if j == 0:
                dp[i][j] = dp[i-1][j] + 1
            else: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        else: dp[i][j] = dp[i-1][j]
print(dp[-1][-1])