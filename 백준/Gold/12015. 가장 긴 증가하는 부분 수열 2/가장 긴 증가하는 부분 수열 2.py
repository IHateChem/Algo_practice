import sys
input = sys.stdin.readline
n = int(input())
D = []
for i in map(int, input().split()):
    l = 0
    r = len(D) - 1
    while l <= r:
        m = (l+r)//2
        if i > D[m]:
            l = m+1
        elif i == D[m]:
            l = m
            break
        else: 
            r = m -1
    if l != len(D):
        D[l] = min(D[l], i)
    else:
        D.append(i)
print(len(D))