import sys
input = sys.stdin.readline
T = int(input().strip())
for _ in range(T):
    N, M = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    A.sort()
    B.sort()
    cnt = 0
    for b in B:
        l = 0
        r = N-1
        while l <= r:
            mid = (l+r) // 2
            if b < A[mid]:
                r = mid -1
            else:
                l = mid + 1
        cnt += N-l
    print(cnt)
