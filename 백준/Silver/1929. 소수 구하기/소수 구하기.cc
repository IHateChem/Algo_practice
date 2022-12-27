#include <iostream>
#include <vector>
using namespace std;
int main() {
	int N, M;
	cin >> M >> N;
	vector<int> primes(N+1, 0);
	primes[1] = 1;
	for (int i = 2; i < N/2+1; i++) {
		if (!primes[i]) {
			int t = 2;
			while (t * i <= N) {
				primes[t * i] = 1;
				t++;
			}
		}
	}
	for (int i = M; i <= N; i++) {
		if (!primes[i]) {
			cout << i << "\n";
		}
		
	}

}