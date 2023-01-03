#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <cmath>
#include <string>
#include <queue>
using namespace std;
bool visited[10000];

int _pow(int i, int j) {
	if (j == 0) return 1;
	if (j == 1) return 10;
	if (j == 2) return 100;
	if (j == 3) return 1000;
}
string bfs(int i, int j) {
	queue<pair<int, string>> q;
	q.push({ i, "" });
	visited[i] = 1;
	int a; string s;
	while (!q.empty()) {
		a = q.front().first;
		s = q.front().second;
		q.pop();
		string t = s;
		int next = a * 2 % 10000;
		if (!visited[a * 2 % 10000]) {
			t.push_back('D');
			q.push({ a * 2 % 10000, t });
			visited[a * 2 % 10000] = true;
			if (next == j) return t;
			t.pop_back();
		}
		next = (a == 0) ? 9999 : a - 1;
		if (!visited[next]) {
			t.push_back('S');
			q.push({ next, t });
			visited[next] = 1;
			if (next == j) return t;
			t.pop_back();
		}
		next = 0;
		int t_i = a;
		for (int i = 0; i < 3; i++) {
			next += t_i % 10 * _pow(10, i + 1);
			t_i /= 10;
		}
		next += t_i % 10;
		if (!visited[next]) {
			t.push_back('L');
			q.push({ next, t });
			visited[next] = 1;
			if (next == j) return t;
			t.pop_back();
		}
		next = 0;
		t_i = a;
		next += t_i % 10 * _pow(10, 3);
		t_i /= 10;
		for (int i = 1; i < 4; i++) {
			next += t_i % 10 * _pow(10, i - 1);
			t_i /= 10;
		}
		if (next) {
			t.push_back('R');
			visited[next] = 1;
			q.push({ next, t });
			if (next == j) return t;
		}

	}
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int N;
	cin >> N;
	string answer;
	for (int i = 0; i < N; i++) {
		for (int ii = 0; ii < 10000; ii++) visited[ii] = 0;
		int A, B;
		cin >> A >> B;
		answer = bfs(A, B);
		cout << answer << endl;
	}
}