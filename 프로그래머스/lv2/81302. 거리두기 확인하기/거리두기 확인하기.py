def solution(places):
    answer = []
    for place in places:
        flag = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] != "P": continue
                stack = [(i,j)]
                visited = set([(i,j)])
                for k in range(2):
                    t = []
                    while stack:
                        x,y=stack.pop()
                        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                            if (0<=x+dx<5 and 0<=y+dy<5) and not (x+dx, y+dy) in visited:
                                if place[x+dx][y+dy] == "P": flag *= 0
                                elif place[x+dx][y+dy] == "X": continue
                                else:
                                    visited.add((x+dx,y+dy))
                                    t.append((x+dx,y+dy))
                    stack = t
        answer.append(flag)         
    return answer