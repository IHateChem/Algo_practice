import sys
import heapq
input = sys.stdin.readline

N, M, K = map(int, input().split())
nums = []

for _ in range(N):
    nums.append(int(input()))
def seg_init(s, e, index):
    '''
    indx : 세그먼트 트리의 것(1부터 시작 주의!)
    '''
    if s == e:
        tree[index] = nums[s-1]
    else:
        m = (s+e)//2
        tree[index] = seg_init(s, m, index*2)*seg_init(m+1, e, index*2+1) %  1000000007
    return tree[index]
def seg_sum(s, e, l, r, index):
    if e < l or r <s :
        return 1
    if l <= s and r  >= e:
        return tree[index]
    mid = (s+e) // 2
    return seg_sum(s, mid, l, r, 2*index)*seg_sum(mid+1, e, l, r, 2*index+1) %  1000000007

def seg_update(s,e, index, set_index, set):
    if s == e:
        tree[index] = set
    else:
        m = (s+e)//2
        if m >= set_index:
            tree[index] = seg_update(s, m, index*2, set_index, set)*tree[index*2+1] %  1000000007
        else: tree[index] = seg_update(m+1, e, index*2+1, set_index, set)*tree[index*2] %  1000000007
    return tree[index]



tree = [0] * (len(nums)*4)
seg_init(1, len(nums), 1)
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        seg_update(1, len(nums),1, b, c)
    elif a == 2:
        print(seg_sum(1, len(nums), b, c, 1))