import sys 
input = sys.stdin.readline
N = int(input())
stack = [int(input())]
answer=  0
for _ in range(N-1):
    a = int(input())
    while stack and a >= stack[-1]:
        stack.pop()
    stack.append(a)
    answer += len(stack) -1
print(answer)