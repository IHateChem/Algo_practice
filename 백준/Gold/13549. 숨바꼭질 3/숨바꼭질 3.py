n, k = map(int, input().split())
history = set()
from collections import deque 
q = deque()
while n < 110000 and not n in history:
    q.append((n,0))
    history.add(n)
    n *= 2
while q:
    x, n = q.popleft()
    if x == k: break
    next = x + 1
    while not next in history and next < 110000:
        q.append((next, n+1))
        history.add(next)
        if next == k:
            n += 1
            break
        next *= 2
    next = x - 1
    while not next in history and next < 110000 and next >= 0:
        q.append((next, n+1))
        if next == k:
            n += 1
            break
        history.add(next)
        next *= 2
print(n)