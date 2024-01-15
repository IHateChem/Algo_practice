N = int(input())
n = 1
squares = [0]
answer = []
squares_dict = {}
while n**2-squares[-1]<=N:
    squares.append(n**2)
    squares_dict[squares[-1]] = n
    n += 1

squares_set = set(squares)
squares_set.remove(0)
for square in squares:
    if square - N in squares_set:
        answer.append(square)
if answer:
    for a in answer:
        print(squares_dict[a])
else:
    print(-1)