def seg_init(s, e, index):
    '''
    indx : 세그먼트 트리의 것(1부터 시작 주의!)
    '''
    if s == e:
        tree[index] = nums[s-1]
    else:
        m = (s+e)//2
        tree[index] = seg_init(s, m, index*2) + seg_init(m+1, e, index*2+1)
    return tree[index]
def seg_sum(s, e, l, r, index):
    if e < l or r <s :
        return 0
    if l <= s and r  >= e:
        return tree[index]
    mid = (s+e) // 2
    return seg_sum(s, mid, l, r, 2*index) + seg_sum(mid+1, e, l, r, 2*index+1)

def seg_update(s,e, index, set_index, set):
    if s == e:
        tree[index] = set
    else:
        m = (s+e)//2
        if m >= set_index:
            tree[index] = seg_update(s, m, index*2, set_index, set) + tree[index*2+1]
        else: tree[index] = seg_update(m+1, e, index*2+1, set_index, set) + tree[index*2]
    return tree[index]

import sys
input = sys.stdin.readline
n = int(input())
nums = [0]*1000001
tree=  [0]*4000004
for i in range(n):
    A = list(map(int, input().split()))
    if len(A) == 3:
        a,b,c = A
    else:
        a,b = A
    if a == 1:
        l = 1
        r = 1000001
        while l < r:
            m = (l+r)//2
            if seg_sum(1, 1000001, l, m, 1) >= b:
                r = m
            else:
                b -= seg_sum(1, 1000001, l, m, 1)
                l = m + 1
        seg_update(1,1000001, 1, r, nums[r]-1)
        nums[r] -= 1
        print(r)
    else:
        seg_update(1,1000001, 1, b, nums[b]+c)
        nums[b]+=c