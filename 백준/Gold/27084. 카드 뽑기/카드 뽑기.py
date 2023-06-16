from collections import defaultdict as dd
N = int(input())
A = list(map(int, input().split()))
def fast_power(a, x):
    if x == 0:
        return 1
    elif x == 1:
        return a
    y = fast_power(a, x >> 1) 
    if x & 1:
        return y * y * a
    else:
        return y * y
numbers = dd(int)
for n in A: numbers[n] += 1
cnt = 1
for v in numbers.values():
    cnt *= v+1
print((cnt-1)%1000000007)