import sys
from collections import defaultdict as dd
input = sys.stdin.readline
N = int(input())
users = []
for _ in range(N):
    a, b = input().rstrip().split()
    a = int(a)
    users.append((a,_ , b))
users.sort()
for a,_,  b in users:
    print(str(a)+" "+b)