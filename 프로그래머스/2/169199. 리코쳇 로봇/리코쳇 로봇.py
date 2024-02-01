def solution(board):
    robot =  [(i,j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == "R"][0]
    goal = [(i,j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == "G"][0]
    q = [robot]
    answer = 0
    inbound = lambda x, y: 0<=x<len(board) and 0<=y<len(board[0])
    t = []; visited = set()
    while q:
        pos = q.pop()
        r, c = pos
        if pos == goal: break
        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
            nr, nc = r+dr, c + dc
            while inbound(nr, nc) and board[nr][nc] !="D":
                nr, nc = nr + dr, nc + dc
            nr, nc = nr - dr, nc - dc
            if not inbound(nr, nc) or (nr, nc) in visited or board[nr][nc] == "D": continue
            visited.add((nr, nc))
            t.append((nr, nc))
        if not q:
            q = t
            t = []
            answer += 1
    else: answer = -1
    return answer