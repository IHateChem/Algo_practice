#일단 아이디어
from collections import defaultdict as dd
history = dd(int)
def mul(a: list, b: list) -> list:
    # get the dimensions of the matrices
    m = len(a)  # number of rows in a
    n = len(b[0])  # number of columns in b

    # create an empty matrix to store the result
    result = [[0 for j in range(n)] for i in range(m)]

    # perform matrix multiplication
    for i in range(m):
        for j in range(n):
            for k in range(len(b)):
                result[i][j] = (result[i][j] + (a[i][k] * b[k][j])) %1000
    return result


def power(a,b):
    if b == 1: return a
    if not history[b]:
        A = power(a, b//2)
        B = power(a, b//2)
        history[b] =  mul(A, B) if b % 2 == 0  else mul(mul(A, B), a)
    return history[b]
N, B = map(int, input().split())
answer = power([list(map(lambda t: int(t) %1000, input().split())) for _ in range(N)], B)
for t in answer:
    print(*t)