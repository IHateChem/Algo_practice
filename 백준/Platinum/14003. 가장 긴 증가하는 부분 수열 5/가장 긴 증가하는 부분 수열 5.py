import sys
from bisect import bisect_left, bisect_right
from collections import deque
input = sys.stdin.readline
n = int(input())
D = []
A = list(map(int, input().split()))
parents = [-1]*len(A)
address = []
for n in range(len(A)):
    i = A[n]
    l = bisect_left(D, i)
    if l != len(D): #이거 ==으로하면 시간초과
        if D[l] > i:
            D[l] = i
            address[l] = n
    else:
        D.append(i)
        address.append(n)
    parents[n] = address[l-1]
print(len(D))
p = address[-1]
answer = deque()
for i in range(len(D)):
    answer.appendleft(A[p])
    p = parents[p]
print(" ".join(map(str, answer)))