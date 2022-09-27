'''
-아이디어: 각네트워크별 딕셔너리 만든후, 친구 새로 추가 될떄마다 딕셔너리 만듬
새로운 곳에 없으면 스택에 추가, 있으면 말고
시간 복잡도 대부분: O(n) 해시 충돌 많이 일어나면 그이상 될수도 있음.


'''

import sys
from collections import defaultdict as dd

input = sys.stdin.readline

N = int(input().strip())
def find(mergenetwork, p):
    while mergenetwork[p] != p:
        p = mergenetwork[p]
    return p
answer = []
for i in range(N):
    F = int(input().strip())
    network = dd(int)
    mergenetwork = dd(int)
    people = dd(int)
    networkindex = 1
    for f in range(F):
        A, B = input().strip().split()
        if people[A]:
            if find(mergenetwork, people[B]) != find(mergenetwork, people[A]):
                if not people[B]:
                    people[B] = find(mergenetwork, people[A])
                    network[people[B]] += 1
                else:
                    n = network[find(mergenetwork, people[B])]
                    mergenetwork[find(mergenetwork, people[B])] = find(mergenetwork, people[A])
                    network[find(mergenetwork, people[B])] += n 
        elif people[B]:
            people[A] = find(mergenetwork, people[B])
            network[people[A]] += 1
        else:
            networkindex += 1
            people[A] = networkindex
            people[B] = networkindex
            mergenetwork[networkindex] = networkindex
            network[networkindex] = 2
        answer.append(network[find(mergenetwork, people[A])])

print("\n".join(list(map(str,answer))).strip("\n"))