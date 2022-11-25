import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
G = int(input()); P = int(input()); answer = 0 
def changeindex(index, g, answer):
    if g < 0 :
        print(answer)
        exit(0)
    if index[g] != index[index[g]]:
        N, answer = changeindex(index, index[g], answer)
    else:
        N = index[g] - 1
        answer += 1
    index[index[g]] = N
    return N, answer
index = [i for i in range(G)]
for _ in range(P):
    g = int(input())
    N, answer = changeindex(index, g-1, answer)
    index[g-1] = N
print(answer)