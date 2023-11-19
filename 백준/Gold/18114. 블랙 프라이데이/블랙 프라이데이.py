N, C = map(int, input().split())
W = sorted(map(int, input().split()))

possible = set()

for x in W:
    possible.add(C - x)
for i in range(N):
    y = W[i]
    if y in possible and y != C - y:
        print(1)
        exit()
    if y > C - W[0]:
        break
    for j in range(i + 1, N):
        z = W[j]
        if y + z in possible and y + z != C - z and y + z != C - y:
            print(1)
            exit()
        if y + z > C:
            break

print(1 if 0 in possible else 0)