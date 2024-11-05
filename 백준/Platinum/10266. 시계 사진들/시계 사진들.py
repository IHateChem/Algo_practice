import sys
input = sys.stdin.readline
N = int(input())    
clock1 = sorted(list(map(int, input().split())))
clock2 = sorted(list(map(int, input().split())))

clock1_diff = [(clock1[i-1]-clock1[i]) % 360000 for i in range(N)]
clock2_diff = [(clock2[i-1]-clock2[i]) % 360000 for i in range(N)]

clock1_diff *= 2

def mkKMPTable(pattern):
    i = 0
    t = [0] * len(pattern)
    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = t[i-1]
        if pattern[i] == pattern[j]:
            i += 1
            t[j] = i
    return t
def check(i):
    for k in range(N//2):
        if clock1_diff[i+k] != clock2_diff[k]:
            return False
    return True
table = mkKMPTable(clock2_diff)
i = 0
j = 0
for i in range(N*2):
    while j > 0 and clock1_diff[i] != clock2_diff[j]:
        j = table[j-1]
        
    if clock1_diff[i] == clock2_diff[j]:
        if j == N-1:
            print("possible")
            exit(0)
        j += 1
print("impossible")