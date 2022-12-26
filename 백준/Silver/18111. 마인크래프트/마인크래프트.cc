#include <iostream>
#include <vector>
using namespace std;
int main() {
	int N, M, B;
	cin >> N >> M >> B;
	int t;
	int minv = 501, maxv = 0;
	double sum = 0;
	vector<vector<int> > MAP (N, vector <int> (M,0));
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> t;
			minv = min(minv, t);
			maxv = max(maxv, t);
			sum += t;
			MAP[i][j] = t;
		}
	}
	double average = sum / (N * M);
	long mintime = 2147483647;
	int height = 0;
	for (int i = maxv; i >= minv; i--) {
		int t = 0;
		int B_t = B;
		for (int k = 0; k < N; k++) {
			for (int j = 0; j < M; j++) {
				if (MAP[k][j] > i) {
					B_t += (MAP[k][j] - i);
					t += (MAP[k][j] - i) * 2;
				}
				else if (MAP[k][j] < i) {
					B_t += (MAP[k][j] - i);
					t += (i-MAP[k][j]);
				}
			}
		}
		if (B_t >= 0) {
			if (mintime > t) {
				mintime =long(t); 
				height = i;
 
			}
		}
	}
	cout << mintime << " " << height;
}