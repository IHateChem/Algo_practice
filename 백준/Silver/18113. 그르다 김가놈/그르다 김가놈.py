import sys
input = sys.stdin.readline
N , K, M = map(int, input().split())
gimbaps = []
for _ in range(N):
    L = int(input())
    if L <= K: pass
    elif L < 2*K:
        gimbaps.append(L-K)
    else:
        gimbaps.append(L-2*K)
l = 1
p = -1
if gimbaps:
    r = max(gimbaps)
    while l <= r:
        mid = (l+r) // 2
        answer = 0
        for gimbap in gimbaps:
            answer += gimbap // mid
        if answer >= M:
            l = mid + 1
            p = mid
        else:
            r = mid - 1
print(p)