from collections import defaultdict as dd
def solution(game_board, table):
    answer = 0
    game_board_db = dd(int)
    inbound = lambda x, y: 0<=x<len(game_board) and 0<=y<len(game_board[0])
    inbound_t = lambda x, y: 0<=x<len(table) and 0<=y<len(table[0])
    def table_dfs(x, y, dx, dy, blocks):
        table[x+dx][y+dy] = 0
        blocks.append((dx,dy))
        for ddx, ddy in ((1,0), (-1,0), (0,1), (0,-1)):
            if inbound_t(x+ddx+dx, y+ddy+dy) and table[x+ddx+dx][y+ddy+dy]:
                table_dfs(x,y,ddx+dx, ddy+dy, blocks)
    def board_dfs(x, y, dx, dy, blocks):
        game_board[x+dx][y+dy] = 2
        blocks.append((dx,dy))
        for ddx, ddy in ((1,0), (-1,0), (0,1), (0,-1)):
            if inbound(x+ddx+dx, y+ddy+dy) and not game_board[x+ddx+dx][y+ddy+dy]:
                board_dfs(x,y,ddx+dx, ddy+dy, blocks)
    def rotation(arr):
        space = zip(*arr[::-1])
        return tuple([tuple(t) for t in space])
        
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            if game_board[i][j]: continue
            blocks = []
            board_dfs(i,j,0,0,blocks)
            min_x = min(map(lambda t: t[0], blocks))
            max_x = max(map(lambda t: t[0], blocks))
            min_y = min(map(lambda t: t[1], blocks))
            max_y = max(map(lambda t: t[1], blocks))
            space = [[0]*(max_y-min_y+1) for _ in range(max_x-min_x+1)]
            for x, y in blocks:
                space[x-min_x][y-min_y] = 1
            space_tuple = tuple([tuple(t) for t in space])
            game_board_db[space_tuple] += 1
        
    for i in range(len(table)):
        for j in range(len(table[0])):
            if not table[i][j]: continue
            blocks = []
            table_dfs(i,j,0,0,blocks)
            min_x = min(map(lambda t: t[0], blocks))
            max_x = max(map(lambda t: t[0], blocks))
            min_y = min(map(lambda t: t[1], blocks))
            max_y = max(map(lambda t: t[1], blocks))
            space = [[0]*(max_y-min_y+1) for _ in range(max_x-min_x+1)]
            for x, y in blocks:
                space[x-min_x][y-min_y] = 1
            space_tuple = tuple([tuple(t) for t in space])
            for _ in range(4):
                if game_board_db[space_tuple]:
                    answer += len(blocks)
                    game_board_db[space_tuple] -= 1
                    break
                space_tuple = rotation(space_tuple)
    return answer 