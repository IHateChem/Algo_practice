import sys
input = sys.stdin.readline
N, M  = map(int, input().split())
lyer = set(list(map(int, input().split()[1:])))
party = []
answer = 0
for _ in range(M):
    p = set(list(map(int, input().split()))[1:])
    party.append(p)
for _ in range(M):
    for p in party:
        for person in p:
            if person in lyer:
                lyer = lyer.union(p)
                break
for p in party:
    if p & lyer:
        continue
    answer += 1
print(answer)