#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <cmath>
#include <string>
#include <queue>
#include <map>
using namespace std;
map <int, int> f_0;
map <int, int> f_1;
int cnt_0, cnt_1;
pair<int, int> fibonacci(int n) {
    if (n == 0) {
        return {1, 0};
    }
    else if (n == 1) {
        return { 0, 1 };
    }
    else if (f_0.find(n) != f_0.end() && f_1.find(n) != f_1.end()) {
        return { f_0[n], f_1[n] };
    }
    else {
        f_0[n] = fibonacci(n - 1).first + fibonacci(n - 2).first;
        f_1[n] = fibonacci(n - 1).second + fibonacci(n - 2).second;
        return { f_0[n], f_1[n] };
    }
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    f_0[0] = 1;
    f_1[1] = 1;
    int a, N;
    pair<int, int> c;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> a;
        cnt_0 = 0; cnt_1 = 0;
        c = fibonacci(a);
        cout << c.first << " " << c.second << '\n';
    }

}