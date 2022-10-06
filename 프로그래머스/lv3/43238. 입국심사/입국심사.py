'''
아이디어: 총시간을 m으로 두고, 그시간내에 검사가능한 사람수 구함사람이 같아질때까지 이분탐색. 
'''
def get_num(times, m):
	num = 0
	for time in times:
		num += m // time
	return num
def solution(n, times):
	answer = 0
	l = min(times)
	r = max(times) * n
	while l <= r:
		m = (l+r)//2
		tempnum = get_num(times, m)
		if tempnum < n:
			l = m + 1
		else:
			r = m - 1
	return l