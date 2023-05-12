import sys
input =sys.stdin.readline
N = int(input())
A = [];B=[];C=[];D=[]
for i in range(N):
    a,b,c,d=map(int, input().split())
    A.append(a);B.append(b);C.append(c);D.append(d)
AB = [];CD=[]
for i in range(N):
    for j in range(N):
        AB.append(A[i]+B[j])
        CD.append(C[i]+D[j])
AB.sort();CD.sort(reverse=True)
pnt1 = 0;pnt2=0
answer = 0
N = len(AB)
while pnt2<N and pnt1 <N:
    if AB[pnt1] + CD[pnt2] == 0 :
        for i in range(pnt1+1, N):
            if AB[pnt1] != AB[i]: break
        else: i+=1
        for j in range(pnt2+1, N):
            if CD[pnt2] != CD[j]: break
        else: j+=1
        answer += (i-pnt1)*(j-pnt2)
        pnt1 = i; pnt2 = j
    elif AB[pnt1] + CD[pnt2] > 0:
        pnt2 += 1
    else:   
        pnt1 += 1 
print(answer)