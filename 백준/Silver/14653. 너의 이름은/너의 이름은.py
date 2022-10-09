#반례: K-1에서 읽고 그뒤론 안읽엇을 수도 있음. 
import sys
import copy
N, K, Q= map(int, sys.stdin.readline().split())
data = {}
tot = set( [chr(65+i) for i in range(1, N)])
idx = -1
idxlist = []
readlist = []
target = -1
for i in range(K):
	R, P = sys.stdin.readline().split()
	R = int(R)
	if idx != R:
		idxlist.append(R)
		idx = R
	if data.get(R):
		data[R].add(P)
	else:
		data[R] = set()
		data[R].add(P)
	if i + 1 == Q:
		target =  R
		targetset = data[R]
	if i+1> Q:
		targetset.add(P)
candidateset =tot - targetset
c = sorted(list(candidateset))
if c and target != 0:
    print(" ".join(c))
else:
    print(-1)