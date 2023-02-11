from collections import defaultdict as dd
def get_pair(n):
    ret = []
    for i in range(1, n//2+1):
        ret.append((i, n-i))
    return ret
def get_possible(n1, n2, n_set, nums):
    n = n1+n2
    for i in n_set[n1]:
        for j in n_set[n2]:
            if not nums[i+j]:
                nums[i+j] = 1
                n_set[n].add(i+j)
            if not nums[i*j]:
                nums[i*j] = 1
                n_set[n].add(i*j)
            if not nums[abs(i-j)]:
                nums[abs(i-j)] = 1
                n_set[n].add(abs(i-j))
            if not nums[-abs(i-j)]:
                nums[-abs(i-j)] = 1
                n_set[n].add(-abs(i-j))
            if j and not nums[i//j]:
                nums[i//j] = 1
                n_set[n].add(i//j)
            if i and not nums[j//i]:
                nums[j//i]= 1
                n_set[n].add(j//i)
    
def solution(N, number):
    numbers = dd(int)
    numbers[N] = 1
    nums_set = [set() for _ in range(9)]
    nums_set[1].add(N)
    if N == number: return 1
    for i in range(2, 9):
        nums_set[i].add(int(str(N)*i))
        numbers[int(str(N)*i)]=1
        for a, b in get_pair(i):
            get_possible(a,b,nums_set,numbers)
        if number in nums_set[i]: return i
    return -1