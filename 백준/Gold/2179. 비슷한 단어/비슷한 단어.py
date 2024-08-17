import sys
input = sys.stdin.readline
N = int(input())
words = [input().strip() for _ in range(N)]
idxes = {1:-1}
answer = []
dictionary = {"": 1}
max_len = 0
idx = 0
for word in words:
    if word in dictionary and dictionary[word] == word:
        continue
    idxes[word] = idx
    idx += 1
    t = 1
    while t <= len(word) and word[:t] in dictionary:
        t += 1
    if max_len < t:
        max_len = t
        answer = [dictionary[word[:t-1]], word]
    elif max_len == t and idxes[answer[0]] > idxes[dictionary[word[:t-1]]]:
        answer = [dictionary[word[:t-1]], word]
    for i in range(1, len(word)+1):
        if word[:i] not in dictionary:
            dictionary[word[:i]] = word
print("\n".join(answer))