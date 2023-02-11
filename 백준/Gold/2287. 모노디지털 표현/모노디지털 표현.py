import sys
input = sys.stdin.readline
def get_pair(n):
    ret = []
    for i in range(1, n//2+1):
        ret.append((i, n-i))
    return ret
def get_possible(n1, n2, n_set):
    n = n1+n2
    for i in n_set[n1]:
        for j in n_set[n2]:
            n_set[n].add(i+j)
            n_set[n].add(i*j)
            n_set[n].add(abs(i-j))
            n_set[n].add(-abs(i-j))
            if j: n_set[n].add(i//j)
            if i: n_set[n].add(j//i)
    
def solution(N, number):
    nums_set = [set() for _ in range(9)]
    nums_set[1].add(N)
    if N == number: return 1
    for i in range(2, 9):
        nums_set[i].add(int(str(N)*i))
        for a, b in get_pair(i):
            get_possible(a,b,nums_set)
        if number in nums_set[i]: return i
    return -1
K = int(input())
N = int(input())
for i in range(N):
    answer = solution(K, int(input()))
    print(answer if answer != -1 else "NO")