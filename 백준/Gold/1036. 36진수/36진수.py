import sys
from collections import defaultdict as dd
import heapq
input = sys.stdin.readline
N=int(input())
wordlist =  []
wordbook= dd(float)
original = {}
stack = []
maxlen = 0
for _ in range(N):
    word = input().strip()
    word = word.lstrip("0")
    wordlist.append(word)
    maxlen = max(len(word), maxlen)
score = {}
for i in range(10):
    score[str(i)] = i
    original[i] = str(i)
for i in range(26):
    score[chr(65+i)] = 10 + i
    original[10+i] = chr(65+i)
for word in wordlist:
    for i, w in enumerate(word):
        wordbook[w] += (35-score[w]) * (36**(len(word)-maxlen-i))
for k, v in wordbook.items():
    heapq.heappush(stack, (-1*v, k))
changeset = set(); cnt = 0
K = int(input())
while stack and cnt < K:
    v, k = heapq.heappop(stack)
    changeset.add(k)
    cnt += 1
answer = [0]*(maxlen+52)
for word in wordlist:
    for i, w in enumerate(word):
        if w in changeset:
            answer[len(word)-1-i] += 35
        else:
            answer[len(word)-1-i] += score[w]
ans = []
for i in range(maxlen+51):
    answer[i+1] += answer[i] // 36
    ans.append(original[answer[i]%36])
ans = "".join(ans).rstrip("0")[::-1]
print(ans if ans != "" else "0")

