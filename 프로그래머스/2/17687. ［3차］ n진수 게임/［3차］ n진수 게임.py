def solution(n, t, m, p):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    answer = '0'
    for i in range(t*m):
        tt = ""
        while i > 0:
            tt = nums[i%n] + tt
            i = i // n
        answer += tt
    ret = ''
    for i in range(t):
        j = p + i * m -1
        ret += answer[j]
    
    return ret