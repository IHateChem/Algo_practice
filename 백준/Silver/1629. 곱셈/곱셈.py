import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())
def square(x, n):
    if n == 1:
        return x
    else:
        t = square(x, n//2)
        return t*t*x % C if n % 2 else t*t % C
print(square(A, B) if B != 1 else A % C)