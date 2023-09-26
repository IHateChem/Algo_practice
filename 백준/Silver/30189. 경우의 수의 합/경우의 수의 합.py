import sys
input=sys.stdin.readline
n,m=map(int,input().split())
answer=0
for i in range(n+m+1):
    for j in range(n+1):
        if j<=i and i-j<=m: answer += 1
print(answer)