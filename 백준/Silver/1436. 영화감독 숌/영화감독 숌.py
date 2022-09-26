'''
-아이디어: 순서대로 수 찾다가 N만날시 탈출
O(n)
느낀점: O(n)판단, 가능한거같으면 고민하지말고 가장 멍청한 방법이 방법일수도 있음!
'''

import sys


input = sys.stdin.readline

N = int(input().strip())
n = 666
count = 0
def getsixnum(n):
    cnt = 0
    while n:
        if n % 10 == 6:
            cnt += 1
        else:
            cnt = 0
        n = n // 10
        if cnt == 3:
            return True
    return False
while True:
    if  getsixnum(n):
        count += 1
    if count == N:
        break
    n += 1
print(n) 
