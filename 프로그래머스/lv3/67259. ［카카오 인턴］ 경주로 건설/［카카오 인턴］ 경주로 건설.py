import heapq
def solution(board):
    N=len(board)
    directions = {1:(0,1), 2:(0,-1), 3: (1,0), 4:(-1,0)}
    corners = {1:(3,4), 2:(3,4), 3:(1,2), 4:(1,2)}
    q = [(0, (0,0, 1)), (0, (0,0, 3))] #(price, (r,c,d))
    visited = set()
    inbound = lambda r,c : 0<=r<N and 0<=c<N
    while q:
        price, (r,c,d) = heapq.heappop(q)
        if (r,c,d) in visited: continue
        if r==N-1 and c ==N-1: return price
        visited.add((r,c,d))
        dr,dc = directions[d]
        if inbound(r+dr,c+dc) and not board[r+dr][c+dc]:
            heapq.heappush(q,(price+100, (r+dr,c+dc,d)))
        for nd in corners[d]:
            dr, dc = directions[nd]
            if inbound(r+dr,c+dc) and not board[r+dr][c+dc]:
                heapq.heappush(q,(price+600, (r+dr,c+dc,nd)))