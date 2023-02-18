import sys
input = sys.stdin.readline
N = int(input())
guilty = list(map(int,input().split()))
R = []
for _ in range(N):
    R.append(list(map(int,input().split())))
who = int(input())
alives = set(range(N))
def day(a):
    if len(alives) == 1:
        print(a)
        exit(0)
    target = -1; target_value = -10000
    for i, g in enumerate(guilty):
        if target_value < g and i in alives:
            target = i
            target_value = g
    if target == who: return a
    alives.remove(target)
    if len(alives) == 1:
        print(a)
        exit(0)
    answer = night(a)
    alives.add(target)
    return answer
def night(a):
    answer = a
    for i in range(N):
        if i not in alives: continue
        if i != who:
            alives.remove(i)
            for j in range(N):
                guilty[j] += R[i][j]
            answer = max(day(a+1), answer)
            for j in range(N):
                guilty[j] -= R[i][j]
            alives.add(i)
    return answer
if N % 2 ==0: print(night(0))
else: print(day(0))