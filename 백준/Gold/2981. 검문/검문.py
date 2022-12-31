import sys
from collections import deque
import heapq
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()
diff = []
for i in range(N-1):
    diff.append(nums[i+1]-nums[i])

import math
answer = math.gcd(*diff)
ans = []
for i in range(2,answer+1):
    if answer % i == 0: ans.append(str(i))
print(" ".join(ans))