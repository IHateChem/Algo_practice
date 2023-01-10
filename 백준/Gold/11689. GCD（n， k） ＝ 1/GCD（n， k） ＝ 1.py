import sys
input = sys.stdin.readline
N = int(input())
k = 2
t = N
answer = N
while k <= t**0.5:
    if t % k == 0:
        answer *= (1-1/k)
        while t % k == 0:
            t //= k
    k += 1
if t > 1:
    answer *= (1-1/t)
print(int(answer))