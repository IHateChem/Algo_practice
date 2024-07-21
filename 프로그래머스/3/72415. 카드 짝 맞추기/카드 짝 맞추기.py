from collections import defaultdict as dd
from itertools import permutations as P
import heapq

history = dd(int)
def recursively(keys,visited, pos, dist, board, r, c):
    if len(visited) == len(keys): return dist
    t = 10000000
    for key in keys:
        if key in visited: continue
        visited.add(key)
        for i in range(2):
            start = pos[key][i]
            end = pos[key][not i]
            dt = getDist(board, r, c, *start) + getDist(board, *start, *end)
            board[start ] = 0
            board[end] = 0
            t = min(t, recursively(keys, visited,pos, dist+ dt + 2, board, *end))
            board[start ] = 1
            board[end] = 1
        visited.remove(key)
    return t
            
            
        
    
def getDist(board, r,c, x,y):
    dist = dd(lambda: 10000)
    visited = set()
    dist[(r,c)]= 0
    heap = [(0, r,c)]
    while heap:
        s, r,c = heapq.heappop(heap)
        if (r,c) in visited: continue
        if r == x and c == y: break
        visited.add((r,c))
        for dr, dc in ((1,0),(-1,0), (0,1), (0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <=nr < 4 and 0<=nc<4 and not (nr, nc) in visited and s + 1 < dist[(nr, nc)]:
                heapq.heappush(heap, (s+1, nr, nc))
                dist[(nr, nc)] =  s + 1
            while 0 <=nr < 4 and 0<=nc<4 and not board[(nr,nc)]:
                nr +=dr
                nc += dc
            if not (0 <=nr < 4 and 0<=nc<4):
                nr -= dr
                nc -= dc
            if (nr != r or nc != c) and not (nr, nc) in visited and s +1 < dist[(nr, nc)]:
                heapq.heappush(heap,(s+1, nr, nc))
                dist[(nr, nc)] = s + 1
    return s
                
def solution(board, r, c):
    
    pos = dd(list)
    answer = 1000000000
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                pos[board[i][j]].append((i,j))
    coordiate2card=dd(lambda: 0)
    for key, values in pos.items():
        for value in values:
            coordiate2card[value] = 1
    return recursively(pos.keys(),set(), pos, 0, coordiate2card, r, c)