import sys
input=sys.stdin.readline
dices=list(map(int,input().split()))
graph = [[1], [2], [3], [4], [5],
         [6, 21], [7], [8], [9], [10],
         [11, 25], [12], [13], [14], [15],
         [16, 27], [17], [18], [19], [20],
         [32], [22], [23], [24], [30],
         [26], [24], [28], [29], [24],
         [31], [20], [32]]

score = [0, 2, 4, 6, 8,
         10, 12, 14, 16, 18,
         20, 22, 24, 26, 28,
         30, 32, 34, 36, 38,
         40, 13, 16, 19, 25,
         22, 24, 28, 27, 26,
         30, 35, 0]
players=[0]*4
def moveFirst(pos, scale):
    if len(graph[pos]) == 2:
        return moveSecond(graph[pos][1], scale -1)
    else:
        return moveSecond(graph[pos][0], scale -1)
def moveSecond(pos, scale):
    if not scale or pos ==32: return pos
    return moveSecond(graph[pos][0], scale -1)
answer=0
def back(dept, result):
    if dept == 10:
        global answer
        answer = max(answer, result)
    else:
        scale = dices[dept]
        for i in range(4):
            pos = players[i]
            next = moveFirst(pos, scale)
            if next == 32 or (next < 32 and not next  in players):
                before =  players[i]  
                players[i] = next
                back(dept + 1, result + score[next])
                players[i] = before
back(0,0)
print(answer)