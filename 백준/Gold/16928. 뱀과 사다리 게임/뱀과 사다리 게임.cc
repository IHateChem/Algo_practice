#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <cmath>
#include <string>
#include <queue>
using namespace std;
vector<int> t;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int N, M, a, b;
	cin >> N >> M;
	vector<int>  graph(101, -1);
	vector<int> visited(101, 0);
	for (int i = 0; i < N; i++) {
		cin >> a >> b;
		graph[a] = b;
	}
	for (int i = 0; i < M; i++) {
		cin >> a >> b;
		graph[a] =  b;
	}
	int pnt = 1, cnt = 1, c = 0;
	vector<int> stack;
	stack.push_back(pnt);
	while (1) {
		pnt = stack.back();
		stack.pop_back();
		for (int i = 1; i < 7; i++) {
			if (graph[pnt + i] == -1) {
				t.push_back(pnt + i);
				c = pnt + i;
			}
			else {
				t.push_back(graph[pnt + i]);
				c = graph[pnt + i];
			}
			if (visited[c]) t.pop_back();
			else visited[c] = 1;
			if (c == 100) break;

		}
		if (c == 100) break;
		if (stack.empty()) {
			stack = t;
			cnt++;
			t = vector<int>();
		}
	}
	cout << cnt;
}