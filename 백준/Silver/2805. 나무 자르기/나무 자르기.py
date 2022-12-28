import sys
input = sys.stdin.readline
N , M = map(int, input().split())
trees = list(map(int, input().split()))
l = 0
r = max(trees)
while l <= r:
    m = (l+r) // 2
    t = 0
    for tree in trees: t += tree-m  if tree- m >=0 else 0
    if t >= M:
        l = m + 1
        answer = m
    else:
        r = m - 1
print(answer)