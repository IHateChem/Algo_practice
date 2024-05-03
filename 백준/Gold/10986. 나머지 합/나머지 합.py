N,M=map(int,input().split())
A = map(int,input().split())
sumA = [0]
for a in A:
    sumA.append(sumA[-1]+a)
mod = {i : 0 for i in range(M)}
for j in range(N):
    mod[sumA[j+1]%M] += 1
answer = 0
for i in range(M):
    answer += mod[i] * (mod[i] -1) //2
print(answer+mod[0])