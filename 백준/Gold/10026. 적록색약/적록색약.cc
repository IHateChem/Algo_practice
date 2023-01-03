#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;
char graph[102][102];
bool visited[102][102];
int color_id(char c, bool isrg) {
	if (isrg && (c == *"R" || c == *"G")) {
		return 1;
	}
	if (c == *"R") return 1;
	if (c == *"G") return 2;
	if (c == *"B") return 3;
	if (c == *"C") return 4;
}
void bfs(int i, int j, bool isrg){
	int c = color_id(graph[i][j], isrg);
	vector<pair<int, int>> stack;
	stack.push_back({ i, j });
	visited[i][j] = true;
	while (stack.size() != 0) {
		int a = stack.back().first;
		int b = stack.back().second;
		stack.pop_back();
		if (!visited[a + 1][b] && c == color_id(graph[a+1][b], isrg)) {
			stack.push_back({ a + 1, b });
			visited[a + 1][b] = true;
		}
		if (!visited[a - 1][b] && c == color_id(graph[a - 1][b], isrg)) {
			stack.push_back({ a - 1, b });
			visited[a -1][b] = true;
		}
		if (!visited[a][b+1] && c == color_id(graph[a ][b+1], isrg)) {
			stack.push_back({ a , b+1 });
			visited[a ][b+1] = true;
		}
		if (!visited[a][b-1] && c == color_id(graph[a][b-1], isrg)) {
			stack.push_back({ a, b -1});
			visited[a ][b-1] = true;
		}
	}
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int N;
	cin >> N;

	for (int i = 0; i < N + 2; i++) {
		for (int j = 0; j < N + 2; j++) {
			graph[i][j] = *"C";
		}
	}
	for (int i = 1; i < N+1; i++) {
		for (int j = 1; j < N+1; j++) {
			cin >> graph[i][j];
		}
	}
	for (int i = 0; i < N + 2; i++) {
		for (int j = 0; j < N + 2; j++) {
			visited[i][j] = 1;
		}
	}
	int num_norm = 0, num_rg = 0;
	for (int i = 1; i < N + 1; i++) {
		for (int j = 1; j < N + 1; j++) {
			visited[i][j] = 0;
		}
	}
	for (int i = 1; i < N + 1; i++) {
		for (int j = 1; j < N + 1; j++) {
			if (!visited[i][j]) {
				bfs(i, j, false);
				num_norm++;
			}
		}
	}
	for (int i = 1; i < N + 1; i++) {
		for (int j = 1; j < N + 1; j++) {
			visited[i][j] = 0;
		}
	}
	for (int i = 1; i < N + 1; i++) {
		for (int j = 1; j < N + 1; j++) {
			if (!visited[i][j]) {
				bfs(i, j, true);
				num_rg++;
			}
		}
	}
	cout << num_norm << " " << num_rg;
}