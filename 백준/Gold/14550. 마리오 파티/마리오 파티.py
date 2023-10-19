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
        dp = [0] + [INF] *N + [INF]
        next = set([(0,0)])
        t = set()
        for _ in range(T):
            while next:
                score, s = next.pop()
                for i in range(S):
                    if s+i+1>N+1: break
                    if dp[s+i+1] < score + MAP[s+i]:
                        dp[s+i+1] = score + MAP[s+i]
                        t.add(s+i+1)
            for i in t:
                next.add((dp[i], i))
            t = set()
        print(dp[-1])
except :
    pass
    