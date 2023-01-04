#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <cmath>
#include <string>
#include <queue>
using namespace std;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int N, a;
	cin >> N;
	int pnt = 0;
	bool flag = true;
	vector <int> stack;
	cin >> a;
	vector <bool> answer;
	while (a != pnt) {
		stack.push_back(++pnt);
		answer.push_back(true);
	}
	stack.pop_back();
	answer.push_back(false);
	while (!(stack.empty()&& pnt == N)) {
		cin >> a;
		if (stack.empty()) {
			while (a != pnt && pnt <= N) {
				stack.push_back(++pnt);
				answer.push_back(true);
			}
			if (pnt > N) {
				flag = false;
				break;
			}
			stack.pop_back();
			answer.push_back(false);
		}
		else if (stack.back() == a) {
			stack.pop_back();
			answer.push_back(false);
		}
		else if (stack.back() < a) {
			while (a != pnt && pnt <= N) {
				stack.push_back(++pnt);
				answer.push_back(true);
			}
			if (pnt > N) {
				flag = false;
				break;
			}
			stack.pop_back();
			answer.push_back(false);
		}
		else {
			flag = false;
			break;
		}
	}
	if (flag) {
		for (bool i : answer) {
			if (i) cout << '+' << '\n';
			else cout << '-' << '\n';
		}
	}
	else {
		cout << "NO";
	}
}