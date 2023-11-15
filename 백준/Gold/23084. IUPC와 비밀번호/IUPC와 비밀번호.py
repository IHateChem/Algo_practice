import sys 
from collections import defaultdict as dd
input = sys.stdin.readline
S = input().strip()
N = int(input())
alpha_set = set([w for w in S])
count = dd(int)
for w in S: count[w] += 1
def correct(flag):
    t = dd(int)
    for v in count.values():
        if abs(v)> 1 or t[v]: return False
        if not v: continue
        t[v] += 1
    if t[-1] and not t[1]: return False
    if not t[-1] and not t[1] and flag: return False
    return True
def check(T):
    for s in range(len(S)):
        w = T[s]
        if w in alpha_set:
            count[w] -= 1
    if correct(len(T) == len(S)):
        for s in range(len(S)):
            w = T[s]
            if w in alpha_set:
                count[w] += 1
        return True
    for s in range(len(S), len(T)):
        w = T[s]
        if w in alpha_set:
            count[w] -= 1
        w = T[s-len(S)]
        if w in alpha_set:
            count[w] += 1
        if correct(len(T) == len(S)):
            for i in range(len(S)):
                w = T[s-i]
                if w in alpha_set:
                    count[w] += 1
            return True
    for i in range(len(S)):
        w = T[len(T)-1-i]
        if w in alpha_set:
            count[w] += 1
    return False
    
for _ in range(N):
    T = input().strip()
    if len(S) > len(T):
        print("NO")
        continue
    if check(T):
        print("YES")
    else:
        print("NO")
        