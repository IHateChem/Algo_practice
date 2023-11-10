def checkEqual(p):
    left = 0
    for w in p:
        if w == "(": left += 1
        elif left: left -= 1
        else: break
    else:
        return 1
    return 0
def solution(p):
    left = 0
    if checkEqual(p): return p
    return transform(p)
def reverse(p):
    if not p: return ""
    t = []
    for w in p:
        if w == "(": t.append(")")
        else: t.append("(")
    return "".join(t)
def transform(p):
    if checkEqual(p): return p
    left = 0
    t = []
    u = ""
    tv = []
    v = ""
    for w in p:
        if not u:
            if w == "(": left += 1
            else: left -= 1
            t.append(w)
        else:
            tv.append(w)
        if not left:
            u = "".join(t)
    u = "".join(t)
    v = "".join(tv)
    if checkEqual(u): return u + transform(v)
    return "(" +  transform(v) + ")"+reverse(u[1:-1])
        
            
        