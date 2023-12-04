import sys
from collections import defaultdict as dd
input=sys.stdin.readline
N,M=map(int,input().split())
weight = [list(map(int,input().split())) for _ in range(N)]
dic= dd(list)
for w, p in weight:
    dic[p].append(w)
items = sorted(dic.items())
tot = 0 
answer = 214748348
flag = False
for p, weights in items:
    if tot + sum(weights) < M:
        tot += sum(weights)
    elif flag:
        answer = min(p, answer)
        break
    else:
        flag = True
        answer = 0
        for w in sorted(weights, reverse=True):
            if tot + w < M:
                tot += w
                answer += p
            else:
                answer += p
                break
print(answer if answer != 214748348 else -1)