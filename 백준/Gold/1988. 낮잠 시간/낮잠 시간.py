import sys
input = sys.stdin.readline
N,B = map(int,input().split())
sleeps = [int(input()) for _ in range(N)]
dp1 = [[0] *( B+1 )for _ in range(N)]
dp2 = [[-300000000] *( B +1 )for _ in range(N)]
dp2[0][1] = 0
for n in range(N-1):
    for b in range(B):
        dp2[n+1][b+1] = max(dp1[n][b], dp2[n][b] + sleeps[n+1])
        dp1[n+1][b] = max(dp1[n][b], dp2[n][b])
    dp1[n+1][B] = max(dp1[n][B], dp2[n][B])
print(max([dp2[i][-1] for i in range(N)]))