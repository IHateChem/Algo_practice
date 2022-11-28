import sys
import heapq
input = sys.stdin.readline
N = int(input())
def check(sdk):
    for m in range(9):
        t = set()
        for n in range(9):
            t.add(sdk[m][n])
        for i in range(1, 10):
            if not i in t: return 0
    for n in range(9):
        t = set()
        for m in range(9):
            t.add(sdk[m][n])
        for i in range(1, 10):
            if not i in t: return 0
    for i in range(3):
        for j in range(3):
            t = set()
            for m in range(3):
                for n in range(3):
                    t.add(sdk[i *3 + m][ j*3+ n])
            for ii in range(1, 10):
                if not ii in t: return 0
    return True
for _ in range(N):
    sdk = []
    if _ != 0: input()
    for __ in range(9):
        sdk.append(list(map(int, input().split())))
    answer = "CORRECT" if check(sdk) else "INCORRECT"
    print(f"Case {_+1}: {answer}") 