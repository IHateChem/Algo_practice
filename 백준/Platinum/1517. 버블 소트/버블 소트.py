import sys
import heapq
input = sys.stdin.readline

N= int(input())
def seg_sum(s, e, l, r, index):
    if e < l or r <s :
        return 0
    if l <= s and r  >= e:
        return tree[index]
    mid = (s+e) // 2
    return seg_sum(s, mid, l, r, 2*index) + seg_sum(mid+1, e, l, r, 2*index+1)

def seg_update(s,e, index, set_index):
    if s == e:
        tree[index] += 1
    else:
        m = (s+e)//2
        if m >= set_index:
            tree[index] = seg_update(s, m, index*2, set_index) + tree[index*2+1]
        else: tree[index] = seg_update(m+1, e, index*2+1, set_index) + tree[index*2]
    return tree[index]
from math import ceil,log2
p=N
size=2**ceil(log2(p))
tree=[0]*(size*2)
answer = 0
data = list(map(int, input().split()))
sorted_data = sorted(data)
mapping = {}
for i, d in enumerate(sorted_data):
    mapping[d] = i+1
for d in data:
    answer += seg_sum(1, size, mapping[d]+1, size, 1)
    seg_update(1,size, 1, mapping[d])
print(answer)