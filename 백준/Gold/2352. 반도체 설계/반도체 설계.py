import sys
inputs = lambda: map(int, sys.stdin.readline().split())
N = int(input())
halfcon = list(inputs())
where = [0]
answer = 0
for v in halfcon:
    i = answer
    for i in range(answer, 0, -1):
        if where[i] < v:
            break
    else:
        if answer == 0:
            answer += 1
            where.append(v)
        else:
            where[1] = v
        continue
    if i < answer:
        where[i+1] = v
    else:
        answer += 1
        where.append(v)
print(answer)