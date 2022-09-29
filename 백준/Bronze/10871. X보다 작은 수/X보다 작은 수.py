n, m = map(int,input().split())
l = list(map(int, input().split()))
a = []
for i in l:
    if i < m:
        a.append(i)
print(" ".join(map(str,a)))