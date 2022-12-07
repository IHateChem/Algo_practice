import sys
input = sys.stdin.readline
N, M= map(int, input().split())
f = list(map(int, input().split()))
f_n = []; num_set = set(range(1,N+1)); t = []; i = 0; j= 0
index = [0]*N
while num_set:
    if not t: t_num = num_set.pop()
    else: num_set.remove(t_num)
    if f[t_num-1] in num_set:
        t.append(t_num)
        index[t_num-1] = (i, j); j += 1
        t_num = f[t_num-1]
    elif t:
        t.append(t_num)
        f_n.append(t)
        t = []
        index[t_num-1] = (i, j)
        i += 1; j = 0
    else:
        f_n.append([t_num])
        index[t_num-1] = (i, j)
        i += 1
answer = []
M_fn = []
from  math import gcd
def nlcm(num):      
    answer = num[0]
    for n in num:
        answer = n * answer // gcd(n, answer)
    return answer
lcm = nlcm(list(map(len, f_n)))
M = M % lcm
for i in f_n:
    M_fn.append(M % len(i))
for i in range(N):
    t = (M_fn[index[i][0]] + index[i][1]) % len(f_n[index[i][0]])
    answer.append(str(f_n[index[i][0]][t]))
print(" ".join(answer))