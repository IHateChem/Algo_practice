def solution(m, n, puddles):
    MAP = [[0]*m for _ in range(n)]
    puddles = set([(i[1]-1, i[0]-1) for i in puddles])
    MAP[0][0] = 1
    stack = [(0,0)]
    for i in range(n):
        for j in range(m):
            if (i,j) in puddles: continue
            if i-1 >= 0 and not ((i-1,j) in puddles):MAP[i][j] += MAP[i-1][j] 
            if j-1 >= 0 and not ((i,j-1) in puddles): MAP[i][j] += MAP[i][j-1] 
            MAP[i][j] %= 1000000007
    answer = MAP[-1][-1] % 1000000007
    return answer