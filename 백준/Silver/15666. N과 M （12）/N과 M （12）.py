import sys
input = sys.stdin.readline
N, M = map(int, input().split())
inp = sorted(map(int, input().split()))
answer = []; pos = {}; store = set()
for i, n in enumerate(inp):
    pos[n] = i
def product(num):
    if len(answer) == M:
        if not tuple(answer) in store:
            print(" ".join(map(str, answer)))
            store.add(tuple(answer))
        return
    for i in inp[num: N+1]:
        answer.append(i)
        product(pos[i])
        answer.pop()
product(0)