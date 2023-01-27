import sys
input = sys.stdin.readline
N, S = map(int, input().split())
numbers = list(map(int, input().split()))
start = 0
end = 0
SUM = numbers[0]
min_len = 1e6
while 1:
    if SUM < S and end < N-1:
        end += 1
        SUM += numbers[end]
    elif SUM >= S:
        min_len = min(end - start, min_len)
        SUM -= numbers[start]
        start += 1
    else: break
print(min_len +1 if min_len != 1e6 else 0)