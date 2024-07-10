from collections import defaultdict as dd
def find_set(str1:str) -> dict:
    ret = dd(int)
    p = str1[0]
    for c in str1[1:]:
        if p.isalpha() and c.isalpha():
            ret[p+c] += 1
        p = c
    return ret
def inter(set1, set2):
    ret = dd(int)
    for k in set1.keys():
        if k in set2:
            ret[k] = min(set1[k], set2[k])
    return ret
def union(set1, set2):
    ret = dd(int)
    for k in [*set1.keys(),*set2.keys()]:
        ret[k] = max(set1[k], set2[k])
    return ret
    
def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    set1 = find_set(str1)
    set2= find_set(str2)
    inter_set = inter(set1, set2)
    union_set = union(set1, set2)

    
    return int(sum(inter_set.values())/sum(union_set.values()) * 65536) if sum(union_set.values()) else 65536