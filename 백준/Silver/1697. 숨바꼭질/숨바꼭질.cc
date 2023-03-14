#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <cmath>
#include <string>
#include <queue>
#include <map>
using namespace std;
int visited[100001] = {0,};
vector<int> t;
int N, M;
bool move(int n) {
	if (n  < 100000) if (!visited[n + 1]) {
		t.push_back(n + 1);
		visited[n + 1] = 1;
	}
	if (n+1 == M) return true;
	if (n > 0) {
		if (!visited[n - 1]) {
			t.push_back(n - 1);
			visited[n - 1] = 1;
		}
		if (n-1== M) return true;
	}
	if (2 * n <= 100000)if (!visited[2 * n]) {
		t.push_back(2 * n);
		visited[2 * n] = 1;
	}
	if (2*n == M) return true;
	return false;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	visited[N] = 1;
	cin >> N >> M;
	int a, cnt = 0;
	vector<int> stack;
	stack.push_back(N);
	while (!stack.empty()) {
		a = stack.back();
		stack.pop_back();
		if(a==M) break;
		if (move(a)) {
			cnt++;
			break;
		}
		if (stack.empty()) {
			stack = t;
			cnt++;
			t = vector<int>();
		}	
	}
	cout << cnt;


}