#include <iostream>
#include <vector>
using namespace std;
int main() {
	int N;
	cin >> N;
	vector<int> an(N);
	vector<int> bn(N);
	vector<int> cn(N);
	int a, b, c;
	cin >> an[0] >> bn[0] >> cn[0];

	for (int i = 1; i < N; i++) {
		cin >> a >> b >> c;
		an[i] = a + min(bn[i - 1], cn[i - 1]);
		bn[i] = b + min(an[i - 1], cn[i - 1]);
		cn[i] = c + min(bn[i - 1], an[i - 1]);
	}
	cout << min(min(an[N - 1], bn[N - 1]), cn[N - 1]);
	
}