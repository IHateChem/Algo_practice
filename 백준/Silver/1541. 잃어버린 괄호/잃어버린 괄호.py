import sys
input = sys.stdin.readline
exps = input().strip().split("-")
ans = 0
firstterm = exps[0].split("+")
for num in firstterm:
	ans += int(num.lstrip("0"))
if len(exps) > 1:
	for terms in exps[1:]:
		t = 0
		term = terms.split("+")
		for num in term:
			t += int(num.lstrip("0"))
		ans -= t
print(ans)