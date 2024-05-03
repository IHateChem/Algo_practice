def solution(arr):
    answer = -1
    N = len(arr) //2  + 1
    INF = 100000000000
    dp_m = [[INF] *N for _ in range(N)]
    dp_M = [[-INF] *N for _ in range(N)]
    for i in range(N):
        dp_M[i][i] = int(arr[i*2])
        dp_m[i][i] = int(arr[i*2])
    for n in range(1,N):
        for j in range(n):
            for i in range(N-n):
                if arr[(i+j)*2+1] == "+":
                    dp_M[i][i+n] =max(dp_M[i][i+n], dp_M[i][i+j] + dp_M[i+j+1][i+n],  dp_M[i][i+j] + dp_m[i+j+1][i+n],  dp_m[i][i+j] + dp_M[i+j+1][i+n],  dp_m[i][i+j] + dp_m[i+j+1][i+n])
                    dp_m[i][i+n] =min(dp_m[i][i+n], dp_M[i][i+j] + dp_M[i+j+1][i+n],  dp_M[i][i+j] + dp_m[i+j+1][i+n],  dp_m[i][i+j] + dp_M[i+j+1][i+n],  dp_m[i][i+j] + dp_m[i+j+1][i+n])
                else:
                    dp_M[i][i+n] =max(dp_M[i][i+n], dp_M[i][i+j] - dp_M[i+j+1][i+n],  dp_M[i][i+j] - dp_m[i+j+1][i+n],  dp_m[i][i+j] - dp_M[i+j+1][i+n],  dp_m[i][i+j] - dp_m[i+j+1][i+n])
                    dp_m[i][i+n] =min(dp_m[i][i+n], dp_M[i][i+j] - dp_M[i+j+1][i+n],  dp_M[i][i+j] - dp_m[i+j+1][i+n],  dp_m[i][i+j] - dp_M[i+j+1][i+n],  dp_m[i][i+j] - dp_m[i+j+1][i+n])

    return dp_M[0][-1]