def solution(key, lock):
    hole = gethole(lock)
    answer = False
    if not hole:
        answer=  True
    for _ in range(4):
        candidates = getpossible(key, len(lock), len(lock[0]))
        if hole in candidates:
            answer = True
        key = rotate(key)
    return answer

def gethole(key):
    hole = set()    
    for i in range(len(key)):
        for j in range(len(key[0])):
            if not key[i][j]: hole.add((i,j))
    return hole
def getspine(key):
    spine = set()    
    for i in range(len(key)):
        for j in range(len(key[0])):
            if key[i][j]: spine.add((i,j))
    return spine
def getpossible(key, x, y):
    spines = getspine(key)
    endx = x - min(map(lambda t:t[0], spines)); endy =  y - min(map(lambda t:t[1], spines))
    startx = -1 * max(map(lambda t: t[0], spines)); starty=  -1* max(map(lambda t: t[1], spines))
    ret = []
    for i in range(startx, endx):
        for j in range(starty, endy):
            t=  set()
            for tx, ty in spines:
                if -1 < tx + i < x and -1 < ty +j < y:
                    t.add((tx+i, ty+j))
            if t: ret.append(t)
    return ret

def rotate(key):
    return [[key[len(key)-j-1][i] for j in range(len(key))] for i in range(len(key[0]))]