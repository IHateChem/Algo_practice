import sys
input = sys.stdin.readline
K = int(input())
n = int(input())
final = list(map(lambda t: ord(t)-65,input().strip()))
MAP = []; where = 0
for _ in range(n):
    MAP.append(input().strip())
    if MAP[-1][0] == "?": where = _
def checkpossible(ladder):
    p = 0
    for l in ladder:
        if l == "-": p += 1
        else: p = 0
        if p > 1: return False
    return True
def laddering(order, MAP):
    for ladder in MAP:
        for i in range(len(ladder)):
            if ladder[i] == "-":
                order[i], order[i+1] = order[i+1], order[i]
    return order
startingorder = laddering([i for i in range(K)], MAP[:where])
endorder = laddering(final, MAP[where+1:][::-1])
diff_pos = []
answer = ""
for i in range(K-1):
    if startingorder[i] != endorder[i]:
        startingorder[i], startingorder[i+1] = startingorder[i+1], startingorder[i]
        answer += "-"
    else:
        answer += "*"
if checkpossible(answer):
    for i in range(K-1):
        if startingorder[i] != endorder[i]:
            break
    else:
        print(answer)
        exit(0)     
print("x"*(K-1))