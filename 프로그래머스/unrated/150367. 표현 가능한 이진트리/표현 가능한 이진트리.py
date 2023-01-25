def solution(numbers):
    answer = []
    for num in numbers:
        num = decimal2binary(num)
        answer.append(check(num)) 
    return answer
height = [2**i-1 for i in range(1, 20)]
def decimal2binary(nums):
    t = str(bin(nums))[2:]
    for i, n in enumerate(height):
        if n >= len(t): break
    t = "0"*(height[i] - len(t)) + t
    return t
def check(num):
    if len(num) == 1: return 1
    mid = len(num)//2
    if num[mid] == "0":
        return check0(num)
    else:
        l = check(num[:mid])
        r = check(num[mid+1:])
    return l and r
def check0(num):
    for n in num:
        if n == "1": return 0
    return 1
    