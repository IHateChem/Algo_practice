N = int(input())
if N == 1: print(1); 
elif N % 2 == 1: print(-1);
else: print(" ".join(str(i) if i % 2== 0 else str(N-i) for i  in range(N,0,-1)))