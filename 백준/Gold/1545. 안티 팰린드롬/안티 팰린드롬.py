from collections import defaultdict as dd
from math import ceil
word = input()
word_dictionary = dd(int)
for w in word:
    word_dictionary[w] += 1
wd = sorted(list(map(lambda k: list(k), word_dictionary.items())), key = lambda t: t[1])
if len(word_dictionary) == 1 or wd[-1][1] > ceil(len(word)/2):
    if len(word_dictionary) == 1 and wd[0][1] == 1:
        print(word)
    else: print(-1)
    exit(0)
wd.sort()
answer = []
for w, n in wd:
    for i in range(n):
        answer.append(w)
for l in range(len(word) // 2 - 1, -1, -1):
    r = len(word)-l-1
    if answer[l] != answer[r]: continue
    p = r
    while(answer[l] == answer[r]):
        r += 1
    answer[p], answer[r] = answer[r], answer[p]
print("".join(answer))