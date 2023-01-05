#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <cmath>
#include <string>
#include <queue>
using namespace std;
bool visited[102][102];
int graph[102][102][102];
vector < tuple <int, int, int> >  t;
void check(int a, int b, int c, int N, int M, int H) {
	if (a - 1 > 0) {
		if (graph[a - 1][b][c] == 0) {
			graph[a - 1][b][c] = 1;
			t.push_back({ a - 1, b, c });
		}
	}
	if (a < M) {
		if (graph[a + 1][b][c] == 0) {
			graph[a + 1][b][c] = 1;
			t.push_back({ a + 1, b ,c });
		}
	}
	if (b - 1 > 0) {
		if (graph[a][b - 1][c] == 0) {
			graph[a][b - 1][c] = 1;
			t.push_back({ a , b - 1 ,c });
		}
	}
	if (b < N) {
		if (graph[a][b + 1][c] == 0) {
			graph[a][b + 1][c] = 1;
			t.push_back({ a , b + 1,c });
		}
	}
	if (c - 1 > 0) {
		if (graph[a][b][c - 1] == 0) {
			graph[a][b][c - 1] = 1;
			t.push_back({ a, b, c-1 });
		}
	}
	if (c < H) {
		if (graph[a][b][c + 1] == 0) {
			graph[a][b][c + 1] = 1;
			t.push_back({ a, b ,c + 1 });
		}
	}
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int N, M, H;
	int cnt = -1;
	vector<tuple <int, int, int>> stack;
	cin >> N >> M >> H;
	for (int a = 1; a < H + 1; a++) {
		for (int i = 1; i < M + 1; i++) {
			for (int j = 1; j < N + 1; j++) {
				cin >> graph[i][j][a];
				if (graph[i][j][a] == 1) stack.push_back(make_tuple(i, j, a));
			}
		}
	}
	int a, b, c;
	while (!stack.empty()) {
		a = get<0>(stack.back());
		b = get<1>(stack.back());
		c = get<2>(stack.back());
		stack.pop_back();
		check(a, b,c, N, M, H);
		if (stack.empty()) {
			stack = t;
			t = vector < tuple <int, int, int> > ();
			cnt++;
		}	
	}
	for (int a = 1; a < H + 1; a++) {
		for (int i = 1; i < M + 1; i++) {
			for (int j = 1; j < N + 1; j++) {
				if (graph[i][j][a] == 0) {
					cout << -1;
					return 0;
				}
			}
		}
	}
	cout << cnt;
}