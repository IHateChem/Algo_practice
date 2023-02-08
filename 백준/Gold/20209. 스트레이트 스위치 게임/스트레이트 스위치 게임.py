import sys
from collections import defaultdict as dd
input=sys.stdin.readline
N,M = map(int, input().split())
nums = [0]
nums.extend(map(int, input().split()))
history = dd(int)
history[tuple(nums)] = 1
switches = [[0]]
for _ in range(M):
    switches.append(list(map(int, input().split()[1:])))
def copy(a):
    return [i for i in a]
stack = [nums]
t = []
def check(a):
    p = a[1]
    for i in a[2:]:
        if i != p: return False
    return True
answer = 1
if check(nums):
    print(0)
    exit(0)
while stack:
    _nums = stack.pop()
    for n, cubes in enumerate(switches[1:]):
        a = tuple([j if not (i in cubes) else (j+n+1)%5 for i,j in enumerate(_nums)])
        if check(a):
            stack = []
            print(answer)
            exit(0)
        if history[a]: continue
        history[a] = 1
        t.append(a)
    if not stack:
        stack = t
        t = []
        answer += 1
print(-1)