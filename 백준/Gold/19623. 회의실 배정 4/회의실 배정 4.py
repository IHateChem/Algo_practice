import sys

input = sys.stdin.readline
N = int(input())
conferenceset = []    
timeset = set()
for i in range(N):
    t = list(map(int, input().strip().split()))
    conferenceset.append(t)
    timeset.add(t[0])
    timeset.add(t[1])
timelist = sorted(list(timeset))
timedict = {timelist[i]: i for i in range(len(timelist))}
indextable = {}
newconferenceset = []
conferenceset.sort(key=lambda x : (x[1], x[0]))
for i, conference in enumerate(conferenceset):
    t = (timedict[conference[0]], timedict[conference[1]], conference[2])
    newconferenceset.append(t)
    indextable[t[1]] = i + 1
def getindex(n, id):
    i = n
    while 1:
        if i < 0:
            return -1
        if indextable.get(i):
            if indextable[i] <= id:
                return indextable[i] -1
        i -= 1
dp = [0 for i in range(N+1)] 
for i in range(N):
    start = newconferenceset[i][0]
    idx = getindex(start, i)
    dp[i] = max(dp[i-1], dp[idx]+newconferenceset[i][2]) 
print(max(dp))