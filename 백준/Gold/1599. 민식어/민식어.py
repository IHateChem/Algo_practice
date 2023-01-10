import sys
input = sys.stdin.readline
N = int(input())
minsik_dict = {}
alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split() 
for i, w in enumerate("a b k d e g h i l m n z o p r s t u w y".split()):
    minsik_dict[w] = alpha[i]
answer = []
for _ in range(N):
    word = input().strip()
    ans = []
    t = word.replace("ng", "z")
    for w in t:
        ans.append(minsik_dict[w])
    answer.append(("".join(ans), word))
answer.sort()
print("\n".join(map(lambda t: t[1], answer)))