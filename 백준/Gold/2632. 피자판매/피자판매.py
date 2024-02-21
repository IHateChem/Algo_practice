import sys
from collections import defaultdict as dd
from bisect import bisect_left as find
input = sys.stdin.readline
S = int(input())
M,N = map(int,input().split())
aSlices = [int(input()) for _ in range(M)]
bSlices = [int(input()) for _ in range(N)]

def getPossibleDict(num, slices):
    possible = dd(int)
    for x in range(num):
        prefixSum = [0]
        for dx in range(num):
            idx = (x+dx) % num
            prefixSum.append(prefixSum[-1] + slices[idx])
        for p in prefixSum[1:]:
            possible[p] += 1
    return possible

aPossible = getPossibleDict(M, aSlices)
bPossible = getPossibleDict(N, bSlices)
aPossible[0], bPossible[0] = 1, 1
aPossible[sum(aSlices)] , bPossible[sum(bSlices)] = 1, 1
aKeys = sorted(aPossible.keys())

answer = 0 
for a in aKeys:
    if a > S : break
    answer += bPossible[S-a] * aPossible[a]
print(answer)