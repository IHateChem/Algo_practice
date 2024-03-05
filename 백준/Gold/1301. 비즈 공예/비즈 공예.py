from collections import defaultdict as dd
N = int(input())
colors = [int(input()) for _ in range(N)]
tot = sum(colors)
before = {i: {tuple([0 if j != i else 1 for j in range(N)] + [-1]):1} for i in range(N)}
for t in range(tot - 1):
    temp = {i: dd(int) for i in range(N)}
    for j in range(N): #직전 구슬 색
        for info, v in before[j].items(): #직전 가능한 경우들의 정보 (*색사용량, 전전색)
            for k in range(N): #이번에 사용하는 색
                if j == k or info[-1] == k or info[k] == colors[k]: continue
                next_info = tuple([info[m] if m != k else info[m] + 1 for m in range(N)]+[j])
                temp[k][next_info] += v
    before = temp
answer = 0
for i in range(N):
    for info, v in before[i].items():
        answer += v
print(answer)