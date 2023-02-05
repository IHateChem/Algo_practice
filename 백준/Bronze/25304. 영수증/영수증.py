import sys
input=sys.stdin.readline
X = int(input())
N = int(input())
tot = 0
for _ in " "*N:
    a,b=map(int,input().split())
    tot += a*b
print("Yes" if X == tot else "No")