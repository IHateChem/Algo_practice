import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
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
        tree[index] = max(seg_init(s, m, index*2) , seg_init(m+1, e, index*2+1))
    return tree[index]
def seg_sum(s, e, l, r, index):
    if e < l or r <s :
        return 0
    if l <= s and r  >= e:
        return tree[index]
    mid = (s+e) // 2
    return max(seg_sum(s, mid, l, r, 2*index) , seg_sum(mid+1, e, l, r, 2*index+1))

def min_seg_init(s, e, index):
    '''
    indx : 세그먼트 트리의 것(1부터 시작 주의!)
    '''
    if s == e:
        min_tree[index] = nums[s-1]
    else:
        m = (s+e)//2
        min_tree[index] = min(min_seg_init(s, m, index*2) , min_seg_init(m+1, e, index*2+1))
    return min_tree[index]
def min_seg_sum(s, e, l, r, index):
    if e < l or r <s :
        return 10e11
    if l <= s and r  >= e:
        return min_tree[index]
    mid = (s+e) // 2
    return min(min_seg_sum(s, mid, l, r, 2*index) , min_seg_sum(mid+1, e, l, r, 2*index+1))


tree = [0] * (len(nums)*4)
min_tree = [10e6]*(len(nums)*4)
seg_init(1, len(nums), 1)
min_seg_init(1, len(nums), 1)
answer = []
for _ in range(M):
    b, c = map(int, input().split())
    answer.append(str(min_seg_sum(1, len(nums), b, c, 1))+" "+str(seg_sum(1, len(nums), b, c, 1)))
print("\n".join(answer))