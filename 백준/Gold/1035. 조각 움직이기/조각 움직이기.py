MAP = [list(input().strip()) for _ in range(5)]

def checkLinked(tu):
    pieceSet = set(tu)
    linked = set([tu[0]])
    for t in tu:
        if not t in linked:
            flag = False
            if t % 5 != 4 and t + 1 in linked:
                flag = True
            if t // 5 != 4 and t + 5 in linked:
                flag = True
            if t % 5 != 0 and t - 1 in linked:
                flag = True
            if t // 5 != 0 and t - 5 in linked:
                flag = True
            if flag:
                linked.add(t)
                continue
            return False
        if t % 5 != 4 and t + 1 in pieceSet:
            linked.add(t+1)
        if t // 5 != 4 and t + 5 in pieceSet:
            linked.add(t+5)
        if t % 5 != 0 and t - 1 in pieceSet:
            linked.add(t-1)
        if t // 5 != 0 and t - 5 in pieceSet:
            linked.add(t-5)
    return len(tu) == len(linked)
def tolist(sets):
    return tuple(sorted(list(sets)))
def move(tu):
    pieceSet = set(tu)
    ret = []
    for t in tu:
        pieceSet.remove(t)
        if t % 5 != 4 and not t + 1 in pieceSet:
            pieceSet.add(t+1)
            ret.append(tolist(pieceSet))
            pieceSet.remove(t+1)
        if t // 5 != 4 and not t + 5 in pieceSet:
            pieceSet.add(t+5)
            ret.append(tolist(pieceSet))
            pieceSet.remove(t+5)

        if t % 5 != 0 and not t - 1 in pieceSet:
            pieceSet.add(t-1)
            ret.append(tolist(pieceSet))
            pieceSet.remove(t-1)
        if t // 5 != 0 and not t - 5 in pieceSet:
            pieceSet.add(t-5)
            ret.append(tolist(pieceSet))
            pieceSet.remove(t-5)
        pieceSet.add(t)
    return list(filter(lambda t: not t in visited, ret))

visited = set()
start = []
for i in range(5):
    for j in range(5):
        if MAP[i][j] == "*":
            start.append(i*5+j)
visited.add(tuple(sorted(start)))
q = [start]
t = []
answer = 0
while q:
    pieces = q.pop()
    if checkLinked(pieces): break
    nextPices = move(pieces)
    visited.update(nextPices)
    t.extend(nextPices)
    if not q:
        answer += 1
        q = t
        t = []
print(answer)