def solution(s):
    answer = 1000
    if(len(s) == 1): return 1
    p = ""
    for unit in range(1, len(s)//2+1):
        pressed = []
        pressedlen = []
        for idx in range(0, len(s), unit):
            if s[idx:idx+unit] != p:
                p = s[idx:idx+unit]
                pressed.append(p)
                pressedlen.append(1)
            else:
                pressedlen[-1] += 1
        merge = []
        for i in range(len(pressed)):
            if pressedlen[i] == 1:
                merge.append(pressed[i])
            else:
                merge.append(str(pressedlen[i]) + pressed[i])
        t = "".join(merge)
        answer = min(len(t), answer)
    return answer