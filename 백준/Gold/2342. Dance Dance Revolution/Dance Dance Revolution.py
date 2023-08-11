sequence = list(map(int,input().split()))
pos2idx = {(i,j): 5*j+i for i in range(5) for j in range(5)}
idx2pos = {5*j+i:(i,j) for i in range(5) for j in range(5)}
def power(s, e):
    if e == 0: return 0
    if s == e: return 1
    if s == 0: return 2
    if abs(s-e) == 2: return 4
    return 3
INF=1000000
dp =  [[INF]*25 for _ in sequence + [""]]
dp[0][0] = 0
for i in range(len(sequence)):
    next=sequence[i]
    for j in range(25):
        p = dp[i][j]
        if p != INF:
            x,y = idx2pos[j]
            if x!= next:
                dp[i+1][pos2idx[(x, next)]] = min(dp[i+1][pos2idx[(x, next)]], p+power(y,next))
            if y!= next:
                dp[i+1][pos2idx[(next,y)]] = min(dp[i+1][pos2idx[(next, y)]], p+power(x,next))
print(min(dp[-1]))