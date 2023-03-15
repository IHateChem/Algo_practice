import sys
input = sys.stdin.readline
N = int(input())
hw = []
for _ in range(N):
    hw.append(tuple(map(int, input().split())))
hw.sort(key = lambda t: t[1])
d, t = hw.pop()
day = t-d
while hw:
    d, t = hw.pop()
    if t <= day: day = t - d
    else:
        day = day - d
print(day)