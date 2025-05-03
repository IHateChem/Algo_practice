import sys
input = sys.stdin.readline

N = int(input())
parents = [[i for i in range(N+1)] for _ in range(3)]


def union(i, a, b):
    parent = parents[i]
    a = find(i, a)
    b = find(i, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find(i, x):
    parent = parents[i]

    if x != parent[x]:
        parent[x] = find(i, parent[x])
    return parent[x]


Ms = map(int, input().split())
for i, m in enumerate(Ms):
    for _ in range(m):
        a, b = map(int, input().split())
        union(i, a, b)
    for j in range(1, N+1):
        find(i, j)

parent_groups = sorted(
    [[tuple([parents[i][j] for i in range(3)]), j] for j in range(1, N+1)])

parent_group = parent_groups[0][0]
t = [parent_groups[0][1]]
answers = []
for i in range(1, N):
    if parent_groups[i][0] == parent_group:
        t.append(parent_groups[i][1])
        continue
    if len(t) > 1:
        answers.append(sorted(t))
    t = [parent_groups[i][1]]
    parent_group = parent_groups[i][0]
if len(t) > 1:
    answers.append(sorted(t))
answers.sort()
print(len(answers))
for answer in answers:
    print(*answer)
