def solution(board, skill):
    n = len(board)
    m = len(board[0])
    zero = [[0]*(m+1) for _ in range(n+1)]
    for ty, r1, c1, r2, c2, degree in skill:
        if ty == 1:
            zero[r1][c1] -= degree
            zero[r2+1][c2+1] -= degree
            zero[r1][c2+1] += degree
            zero[r2+1][c1] += degree
        elif ty == 2:
            zero[r1][c1] += degree
            zero[r2+1][c2+1] += degree
            zero[r1][c2+1] -= degree
            zero[r2+1][c1] -= degree
    answer = 0
    for i in range(len(board)):
        for m in range(len(board[i])):
            zero[i][m+1] += zero[i][m]
    for m in range(len(board[i])):
        for i in range(len(board)):
            zero[i+1][m] += zero[i][m]
    for i in range(len(board)):
        for m in range(len(board[i])):
            if board[i][m] + zero[i][m] > 0:
                answer += 1
    return answer