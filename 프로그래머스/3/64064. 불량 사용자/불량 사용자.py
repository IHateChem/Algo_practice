import re
def solution(user_id, banned_id):
    answerSet = {}
    answer = 1
    banned_Set = []
    for banned in banned_id:
        regexp = "^"+ banned.replace("*", "[a-z0-9]")+"$"
        t = set()
        for id in user_id:
            if re.match(regexp, id):
                t.add(id)
        banned_Set.append(t)
    lastSet = set()
    def getAnswer(idx, done):
        if idx == len(banned_Set):
            lastSet.add(str(sorted(list(done))))
            return 1
        t = 0
        for id in banned_Set[idx]:
            if id in done: continue
            else:
                done.add(id)
                t += getAnswer(idx+1, done)
                done.remove(id)
        return t
    getAnswer(0, set())
    return len(lastSet)