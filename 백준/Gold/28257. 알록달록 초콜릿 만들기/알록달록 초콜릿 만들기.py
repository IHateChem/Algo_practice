from math import ceil, sqrt
import sys
input=sys.stdin.readline

def main(n):
    l = 1
    r = 2 * 10**9
    k = r
    while l <= r:
        mid = (l + r) // 2
        y = mid * (3 * mid + 1) // 2
        if y < n:
            l = mid + 1
        else:
            r = mid - 1
            k = min(k, mid)
    
    a = n - (k - 1) * (3 * k - 2) // 2
    
    if a <= k:
        line = 3 * k - 2
        b = 3 * a - 2
    elif a <= 2 * k - 1:
        line = 3 * k - 1
        b = 3 * (a - k)
    else:
        line = 3 * k
        b = 3 * (a - 2 * k + 1) - 1

    ans = (line * (line - 1) // 2) + b
    return ans
T = int(input())
for _ in range(T):
    n= int(input())
    if n== 1: print(1)
    else:
        print(main(n))