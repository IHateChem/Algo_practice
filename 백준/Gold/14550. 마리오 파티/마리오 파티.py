import sys
input = sys.stdin.readline
INF=-1100000000000000
try:
    while 1:
        N,S,T = map(int,input().split())
        MAP=[]
        while len(MAP)<N:
            MAP.extend(list(map(int,input().split())))
        MAP += [0]
        dp = [[0] + [INF] *N + [INF] for _ in range(T+1)]
        next = set([(0,0)])
        t = set()
        for i in range(T):
            for j in range(i,N+1):
                for k in range(S):
                    if j+k > N: break
                    dp[i+1][j+k+1] = max(dp[i][j]+MAP[j+k], dp[i+1][j+k+1])
        print(dp[-1][-1])
except :
    pass
    