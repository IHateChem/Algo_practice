import sys
input = sys.stdin.readline
N = int(input())
scobil = list(map(int, input().split()))
scobil.sort()
def pow(i, j):
    if j == 1: return i % 1000000007
    if j == 0: return 1
    if j % 2 == 1: return (i*pow(i, j//2)**2) % 1000000007
    return (pow(i, j//2)**2)% 1000000007
answer = 0
for i in range(N):
    answer += (pow(2, i) - pow(2, N-i-1)) * scobil[i]
print(answer % 1000000007)
