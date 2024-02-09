n,K = map(int,input().split())
dp = [[[set([0]) for a in range(n+1)] for _ in range(n+1)] for i in range(n+1)]
from collections import deque, defaultdict as dd
def find(a,b,c, k):
    dq = deque()
    na, nb, nc = dd(int), dd(int), dd(int)
    tb, tc = 0, 0
    if k <= a * b:
        nc[0] = c
        sum_b = 0
        while k:
            if k >= a:
                nb[a] += 1
                sum_b += 1
                k -= a
            else:
                nb[k] += 1
                sum_b += 1
                k -= k
        nb[0] = b - sum_b
    else:
        nb[a] = b
        t = a + b
        sum_c = 0
        k -= a * b
        while k:
            if k >= t:
                nc[t] += 1
                sum_c += 1
                k -= t
            else:
                nc[k] += 1
                sum_c += 1
                k -= k
        nc[0] = c - sum_c
    answer = ""
    while len(answer) < n:
        while nc[tc]:
            answer += "C"
            nc[tc] -= 1
        if nb[tb]:
            tc += 1
            answer += "B"
            nb[tb] -= 1
            continue
        if a:
            tb += 1
            tc += 1
            a -= 1
            answer += "A"
    print(answer)
    exit(0)
        
for a in range(1, n+1):
    for b in range(n+1):
        if a + b > n: break
        c = n - a - b
        if K <= a*b + (a + b) * c:
            find(a,b,c, K)
print(-1)