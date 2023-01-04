import sys
import math
import heapq
from collections import defaultdict as dd
input = sys.stdin.readline
N = input().rstrip()
num_len = len(N)
N = int(N)
answer = [0] * 10

def getzero(num, n):
    if num % 10**(n-1) >= 10**(n-2):
        return 10**(n-2) + int("1"*(n-2))
    t = num % 10**(n-2)
    a = 0
    if t != 0:
        l = int(math.log10(t)+1) 
        a += (n - l -1)*(t+1)
    else:
        return n-1
    for i in range(l):
        a += 10**i
    return a
def calc(num, n, flag):
    if n == 0 : return [0] * 10
    t = calc(num%(10**(n-1)), n-1, False)
    for i, k in enumerate(t):
        answer[i] += (num//(10**(n-1)))*k
    for i in range(1, num//(10**(n-1))):
        answer[i] += 10**(n-1)
    if n > 2 and num > 10**(n-2):
        answer[0] -= 10**(n-2) + int("1"*(n-2)) - getzero(num, n)
    if num//(10**(n-1)) != 0:
        answer[num//(10**(n-1))] += ((num)%(10**(n-1))+1)
    if n == 1: t = [1]
    else: t = [(n-1)*10**(n-1)+10**(n-1)]
    t.extend([n*10**(n-1)]*9)
    return t
calc(N, num_len, True)
print(" ".join(map(str,answer)))