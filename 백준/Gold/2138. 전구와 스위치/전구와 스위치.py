N=int(input())
change = {"0":"1", "1":"0"}
curr = input().strip()
fin = input().strip()
answer = N + 1
t = 0
case1 = [c for c in curr]# 0 ~ 0
for i in range(1, N-1):
    if case1[i-1] != fin[i-1]:
        t += 1
        case1[i] = change[case1[i]]
        case1[i+1] = change[case1[i+1]]
        case1[i-1] = change[case1[i-1]]
if "".join(case1) == fin:
    answer = min(answer, t)
    
t = 1
case2 = [c for c in curr]# 1 ~ 0
case2[0] = change[case2[0]]
case2[1] = change[case2[1]]
for i in range(1, N-1):
    if case2[i-1] != fin[i-1]:
        t += 1
        case2[i] = change[case2[i]]
        case2[i+1] = change[case2[i+1]]
        case2[i-1] = change[case2[i-1]]
if "".join(case2) == fin:
    answer = min(answer, t)
    
t = 1
case3 = [c for c in curr]# 1 ~ 0
case3[-1] = change[case3[-1]]
case3[-2] = change[case3[-2]]
for i in range(1, N-1):
    if case3[i-1] != fin[i-1]:
        t += 1
        case3[i] = change[case3[i]]
        case3[i+1] = change[case3[i+1]]
        case3[i-1] = change[case3[i-1]]
if "".join(case3) == fin:
    answer = min(answer, t)
t = 2
case4 = [c for c in curr]# 1 ~ 0
case4[0] = change[case4[0]]
case4[1] = change[case4[1]]
case4[-1] = change[case4[-1]]
case4[-2] = change[case4[-2]]
for i in range(1, N-1):
    if case4[i-1] != fin[i-1]:
        t += 1
        case4[i] = change[case4[i]]
        case4[i+1] = change[case4[i+1]]
        case4[i-1] = change[case4[i-1]]
if "".join(case4) == fin:
    answer = min(answer, t)
if answer == N + 1: answer = -1
print(answer)