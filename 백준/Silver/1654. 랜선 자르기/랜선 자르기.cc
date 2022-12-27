#include <iostream>
#include <vector>
using namespace std;
long long int get_max(vector<long long int> v) {
	long long int max_num = 0;
	for (long long int i : v) {
		if (max_num < i) max_num = i;
	}
	return max_num;
}
int main() {
	long long int N, M;
	long long int ans;
	cin >> N >> M;
	vector <long long int> v(N);
	for (int i = 0; i < N; i++) cin >> v[i];
	long long int left = 1, right =  get_max(v);
	while (left <= right) {
		long long int mid = (left + right) / 2;
		long long int t = 0;
		for (long long int i : v) t += i / mid;
		if (t >= M) {
			left = mid + 1;
			ans = mid;
		}
		else right = mid-1;
	}
	cout << ans;

}

