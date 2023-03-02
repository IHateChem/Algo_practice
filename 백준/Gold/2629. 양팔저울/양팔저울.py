import sys
input =sys.stdin.readline
N = int(input())
chus = list(map(int, input().split()))
weigths = set()
target_N = int(input())
target_W = list(map(int, input().split()))
answer = []
dp = [0]*40001
for c in chus:
    t = set()
    for w in weigths:
        t.add(w+c)
        t.add(abs(w-c))
    for w in t:
        dp[w] = 1
        weigths.add(w)
    weigths.add(c)
for w in target_W:
    if w in weigths:
        answer.append("Y")
    else:
        answer.append("N")
print(" ".join(answer))