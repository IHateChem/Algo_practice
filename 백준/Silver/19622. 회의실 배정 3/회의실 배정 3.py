'''
아이디어: dp: i번째를 포함시킬때 최댓값, ndp = i번 포함 X최댓값
시.복: 한번 순회 -> O(n)
변수: dp: int[N], ndp: int[N],  
'''
import sys
input = sys.stdin.readline
N = int(input().strip())
dp = [0] *N
ndp = [0]*N
for i in range(N):
    start, finish, num = map(int, input().strip().split())
    dp[i] = ndp[i-1] + num
    ndp[i] = max(dp[i-1], ndp[i-1])
print(max(dp[-1], ndp[-1]))