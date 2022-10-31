'''
an = (n-1)(an-1 + an-2)
'''
from collections import defaultdict
import sys
input = sys.stdin.readline
T = int(input())
a = [0,1,2,9]
for i in range(T):
    N = int(input())
    for n in range(len(a), N):
        a.append(len(a)*(a[n-1]+a[n-2]))
    print(a[N-1])