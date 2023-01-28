#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;
typedef vector< tuple<int, int> > t_list;
bool compare(tuple<int, int>  a,  tuple<int, int> b){
	if (get<0>(a) < get<0>(b)) return true;
	else if (get<0>(a) > get<0>(b)) return false;
	else if (get<1>(a) < get<1>(b)) return true;
	else return false;
}
int main() {
	int N, K, w, v;
	cin >> N >> K;
	vector < vector <int> > vec (N + 1, vector<int>(K+1, 0));
	t_list A;
	for (int i = 0; i < N; i++) {
		cin >> w >> v;
		A.push_back(tuple<int, int>(w, v));
	}
	for (int k = 1; k <K+1; k++) {
		for (int i = 1; i < N+1; i++) {
			if (get<0>(A[i - 1]) == k) {
				vec[i][k] = get<1>(A[i - 1]);
			}
			else if (get<0>(A[i - 1]) < k) vec[i][k] = max(vec[i - 1][k - get<0>(A[i - 1])] + get<1>(A[i - 1]), vec[i - 1][k]);
			else vec[i][k] = vec[i - 1][k];
		}

	}
	cout << vec[N][K];
}