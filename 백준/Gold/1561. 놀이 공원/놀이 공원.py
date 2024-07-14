from collections import defaultdict as dd
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
times = list(map(int,input().split()))
if M >= N:
    print(N)
    exit(0)
times_dict = dd(list)
for n, t in enumerate(times):
    times_dict[t].append(n+1)
l = 0
r = 60000000000 

def calc(m: int):
    t = []
    cnt = M
    _len = 0
    for n in times_dict.keys():
        cnt += m // n * len(times_dict[n])
        if m % n == 0:
            _len += len(times_dict[n])
            t.append(n)
    if 0 <= cnt - N < _len:
        idx = cnt - N
        possible_play = []
        for k in t:
            possible_play.extend(times_dict[k])
        print(sorted(possible_play, reverse=True)[idx])
        exit(0)
    return cnt

while l <= r:
    m = (l+r) // 2
    if calc(m) < N:
        l = m + 1
    else:
        r = m - 1
