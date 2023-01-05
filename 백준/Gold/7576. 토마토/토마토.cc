#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <cmath>
#include <string>
#include <queue>
using namespace std;
bool visited[1002][1002];
int graph[1002][1002];
vector < pair <int, int> >  t;
void check(int a, int b, int N, int M) {
	if (a -1 > 0) {
		if (graph[a - 1][b] == 0) {
			graph[a - 1][b] = 1;
			t.push_back({ a - 1, b });
		}
	}
	if (a < M) {
		if (graph[a + 1][b] == 0) {
			graph[a + 1][b] = 1;
			t.push_back({ a + 1, b });
		}
	}
	if (b-1 > 0) {
		if (graph[a][b - 1] == 0) {
			graph[a][b-1] = 1;
			t.push_back({ a , b - 1 });
		}
	}
	if (b < N) {
		if (graph[a][b + 1] == 0) {
			graph[a][b + 1] = 1;
			t.push_back({ a , b + 1 });
		}
	}
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int N, M;
	int cnt = -1;
	vector<pair <int, int>> stack;
	cin >> N >> M;
	for (int i = 1; i < M + 1 ; i++) {
		for (int j = 1; j < N + 1; j++) {
			cin >> graph[i][j];
			if (graph[i][j] == 1) stack.push_back({ i, j });
		}
	}
	int a, b;
	while (!stack.empty()) {
		a= stack.back().first;
		b = stack.back().second;
		stack.pop_back();
		check(a, b, N, M);
		if (stack.empty()) {
			stack = t;
			t = vector < pair <int, int> >();
			cnt++;
		}
	}
	for (int i = 1; i < M + 1; i++) {
		for (int j = 1; j < N + 1; j++) {
			if (graph[i][j] == 0) {
				cout << -1;
				return 0;
			}
		}
	}
	cout << cnt;
}