import sys
from collections import defaultdict as dd
input = sys.stdin.readline
T = int(input())
fact = [1]*4000001
M = int(1000000007)
def exp(a, b):
    if b == 0: return 1
    if b == 1: return a % M
    if b % 2 ==0:
        return ((exp(a, b//2)%M)**2) % M
    if b % 2 == 1:
        return ((exp(a, b//2) % M)**2*a)%M
for i in range(1, 4000001):
    fact[i] = fact[i-1] * i % M
for _ in range(T):
    n, m = map(int, input().split())
    print(((exp(((fact[m] % M) * (fact[n-m] % M)) % M, M -2) % M )* fact[n])%M)