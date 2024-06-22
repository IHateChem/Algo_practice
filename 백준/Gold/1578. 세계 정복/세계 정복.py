import sys
input = sys.stdin.readline
N, K = map(int,input().split())
people = list(map(int,input().split()))
r = sum(people)// K
l = 1

def splitGroup(m):
    a = 0
    for p in people:
        a += min(m, p)
    if a >= K * m: return True;
    return False

while l < r -1:
    m = (l+r)//2
    if splitGroup(m):
        l = m
    else: r = m - 1
if(splitGroup(r)):
    print(r)
else:
    print(l)