import sys
input = sys.stdin.readline
N, M = map(int, input().split())
answer = []
def product(num):
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return
    for i in range(num, N+1):
        answer.append(i)
        product(i)
        answer.pop()
product(1)