def solution(triangle):
    n = len(triangle)
    for i in range(n-1, 0 ,-1):
        for m in range(i):
            triangle[i-1][m] += max(triangle[i][m], triangle[i][m+1])
    return triangle[0][0]        