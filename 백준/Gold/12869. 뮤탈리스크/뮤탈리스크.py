import sys
from collections import defaultdict as dd
from itertools import permutations as P
input = sys.stdin.readline
N = int(input())
energy = tuple(map(int, input().split()))
a = (9,3,1)
history = dd(int)
t = []
stack = [energy]
answer = 1
while 1:
    s = stack.pop()
    for i in P(a, len(energy)):
        new_energy = tuple(pair[0] - pair[1] for pair in zip(s, i))
        if not history[new_energy]:
            b = 0
            for k in new_energy:
                if k <= 0:
                    b+= 1
            if b == len(i):
                print(answer)
                exit(0)
            t.append(new_energy)
            history[new_energy] = 1
    if not stack:
        stack = t
        answer += 1
        t = []
print(answer)