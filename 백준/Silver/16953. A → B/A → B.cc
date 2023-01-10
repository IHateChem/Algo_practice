#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <cmath>
#include <string>
#include <queue>
#include <map>
using namespace std;
queue<pair<long long, int> > graph;
int N, M;
int bfs() {
	if (graph.empty()) return -2;
	long long t = graph.front().first;
	int k = graph.front().second;
	graph.pop();
	if (M == t) return k;
	long long n1 = t * 2;
	long long n2 = t * 10 + 1;
	if (n1 <= M) {
		if (n1 == M) return k + 1;
		graph.push({ n1, k + 1 });
	}
	if (n2 <= M) {
		if (n2 == M) return k + 1;
		graph.push({ n2, k + 1 });
	}
	
	return bfs();
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N >> M;
	graph.push({ N, 0 });
	cout << bfs() + 1;
}