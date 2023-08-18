import sys
input=sys.stdin.readline
N=int(input())
name2idx = {}
id = 0
for i in range(N):
    name = input().strip()
    name2idx[name] = id
    id += 1
id = 0
answer=0
check = set()
for i in range(N):
    name = input().strip()
    if name2idx[name] > id:
        check.add(name2idx[name])
        answer += 1
    else:
        check.add(id)
        while id in check:
            id += 1
print(answer)