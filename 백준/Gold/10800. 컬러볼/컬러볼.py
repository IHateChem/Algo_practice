import sys
from bisect import bisect_left as bs
from collections import defaultdict as dd
input=sys.stdin.readline
balls=[]
ball_classified=dd(list)
ball_sum=dd(list)
total_sum=[0]
ball_sizes=[]
N=int(input())
def Count(size, color):
    i = bs(ball_classified[color], size)
    return ball_sum[color][i]

for _ in range(N):
    c,s=map(int,input().split())
    ball_classified[c].append(s)
    balls.append((c,s))
    ball_sizes.append(s)
ball_sizes.sort()
for i, s in enumerate(ball_sizes):
    total_sum.append(total_sum[i] + s)
for color in ball_classified.keys():
    ball_classified[color].sort()
    ball_sum[color].append(0)
    for i, size in enumerate(ball_classified[color]):
        ball_sum[color].append(ball_sum[color][i]+size)
for c, s in balls:
    i = bs(ball_sizes, s)
    answer= total_sum[i]
    answer -= Count(s, c)
    print(answer)