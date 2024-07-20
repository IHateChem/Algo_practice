def file2HNT(file):
    stage = 0
    ret = [[],[],[]]
    for c in file:
        if stage == 0 and c.isnumeric():
            stage = 1
        elif stage == 1 and (c.isalpha() or c == "." or c == '-' or c == ' '):
            stage = 2
        ret[stage].append(c.lower())
    r2 = "".join(ret[1]).lstrip("0")
    return ret[0], int(r2 if r2 else "0"), ret[2]
            
def solution(files):
    answer = []
    HNTs = [(file2HNT(file), n) for n, file in enumerate(files)]
    return [files[i] for _, i in sorted(HNTs, key = lambda t: (t[0][0], t[0][1]))]