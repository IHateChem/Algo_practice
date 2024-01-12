def solution(a):
    answer = set()
    leftMin = 1000000001
    rightMin = 1000000001
    for i in range(len(a)):
        if a[i] < leftMin:
            answer.add(a[i])
            leftMin = a[i]
        if a[len(a)-1-i] < rightMin:
            answer.add(a[len(a)-1-i])
            rightMin = a[len(a)-1-i]
    return len(answer)