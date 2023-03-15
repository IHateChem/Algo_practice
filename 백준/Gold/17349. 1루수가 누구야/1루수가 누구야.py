import sys
input = sys.stdin.readline
says = [tuple(map(int, input().split())) for i in range(9)]
can = set()
for i in range(9):
    not1 = set()
    yes1 = set()
    for j in range(9):
        if i == j:
            if not says[j][0]:
                if says[j][1] in not1: break
                else: yes1.add(says[j][1])
            else:
                if says[j][1] in yes1: break
                else: not1.add(says[j][1])
        else:
            if says[j][0]:
                if says[j][1] in not1: break
                else: yes1.add(says[j][1])
            else:
                if says[j][1] in yes1: break
                else: not1.add(says[j][1])
    else:
        if len(yes1) == 1:
            can.add(yes1.pop())
        elif len(not1) == 8:
            for i in range(1,10):
                if not i in not1:
                    can.add(i)
                    break
        elif not yes1:
            print(-1)
            exit()
if len(can) == 1: print(can.pop())
else: print(-1)