import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
password = {}
for _ in range(N):
    a, b = input().rstrip().split()
    password[a] = b
for _ in range(M):
    a = input().rstrip()
    print(password[a])