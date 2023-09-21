import sys
lowerAlpha = set([chr(i) for i in range(97,123)])
sortedLowerAlpha = sorted(list(lowerAlpha))
numbers=set([str(i) for i in range(10)])
try:
    while 1:
        idx=0
        molecule= sys.stdin.readline().strip()
        if(molecule == ""): break
        t = []
        i = 0
        while i < len(molecule):
            m = molecule[i]
            i += 1
            if m in numbers:
                while i < len(molecule) and molecule[i] in numbers:
                    m += molecule[i]
                    i+=1
                m=int(m)
            elif not m in ("(",")"):
                while i < len(molecule) and molecule[i] in lowerAlpha:
                    m += molecule[i]
                    i+=1
            t.append(m)
        stack=[]
        done=[]
        from collections import defaultdict as dd
        count=dd(int)
        n = 0
        while n<len(t):
            m = t[n]
            n += 1
            if m == "(":
                stack.append(m)
            elif m == ")":
                if(n<len(t) and type(t[n]) == int):
                    t_num=t[n]
                    n+=1
                else:
                    t_num=1
                word=[]
                while stack:
                    s = stack.pop()
                    if s == "(": break
                    if type(s) == int: s *= t_num
                    elif not word or type(word[-1]) != int: word.append(t_num)
                    word.append(s)
                j = 0
                word.reverse()
                if stack:
                    for w in word:
                        stack.append(w)
                else:
                    while j in range(len(word)):
                        t_num=1
                        atom = word[j]
                        j += 1
                        if j < len(word) and type(word[j]) == int:
                            t_num=word[j]
                            j+=1
                        count[atom] += t_num
            else:
                if stack: stack.append(m)
                else:
                    t_num=1
                    if n < len(t) and type(t[n]) == int:
                        t_num=t[n]
                        n+=1
                    count[m] += t_num
        answer=[]
        for k, v in sorted(count.items()):
            if v ==1: answer.append(str(k))
            else:answer.append(str(v)+k)
        print("+".join(answer))
except:
    exit(0)