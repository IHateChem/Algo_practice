from collections import defaultdict as dd
def solution(msg):
    answer = []
    wordDict = dd(int)
    for i in range(26):
        wordDict[chr(65+i)] = 1+i
    idx = 27
    p = ""
    i = 0
    def getMsg(p, i):
        if i < len(msg) - 1:
            return p + msg[i], msg[i+1]
        elif i == len(msg)-1:
            return p + msg[i], ""
        else: return 0, 0
    for i in range(len(msg)+1):
        w, c = getMsg(p, i)
        if not (w or c):
            if p != "": answer.append(wordDict[p])
            break
        if wordDict[w+c]:
            p = w
        else:
            wordDict[w+c] = idx
            idx += 1
            p = ""
            answer.append(wordDict[w])
    
    return answer