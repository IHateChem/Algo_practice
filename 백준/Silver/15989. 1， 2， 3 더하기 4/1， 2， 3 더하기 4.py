import sys
input = sys.stdin.readline
N = int(input().strip())
t = [0]*100001
index = 5
for i in range(6):
    t[i] = i
for i in range(N):
    num = int(input().strip())
    for l in range(num+1):
        if l > index:
            t[l] = 1+t[l-2] + t[l-3] - t[l-5]
            index += 1
    print(t[num]) 
    