#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <cmath>
#include <string>
#include <queue>
#include <map>
using namespace std;
int visited[52][52];
int graph[52][52];

int N, M;
int check(int a, int b) {
	visited[a][b] = 1;
	if (!graph[a][b]) return 0;
	if (!visited[a - 1][b]) {
		check(a - 1, b);
	}
	if (!visited[a][b+1]) {
		check(a, b+1);
	}
	if (!visited[a][b-1]) {
		check(a, b-1);
	}
	if (!visited[a+1][b]) {
		check(a+1, b);
	}
	return 1;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int T,K, x, y;
	cin >> T;
	for (int _ = 0; _ < T; _++) {
		cin >> N >> M >> K;
		fill(&graph [0][0], &graph [51][51], 0);
		fill(&visited[0][0], &visited[51][51], 1);
		for (int i = 1; i <= M; i++) {
			for (int j = 1; j <= N; j++) {
				visited[i][j] = 0;
				}
			}
		for (int i = 0; i < K; i++) {
			cin >> x >> y;
			graph[y+1][x+1] = 1;
		}
		int cnt = 0;
		for (int i = 1; i <= M; i++) {
			for (int j = 1; j <= N; j++) {
				if (!visited[i][j]) {
					cnt += check(i, j);
				}
			}
		}
		cout << cnt << "\n";
	}
}