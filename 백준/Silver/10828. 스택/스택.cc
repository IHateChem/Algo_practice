#include <iostream>
#include <vector>

using namespace std;
int main() {
	int N;
	cin >> N;
	int t;
	string order;
	vector<int> stack;
	for (int i = 0; i < N; i++) {
		cin >> order;
		if (order == "push") {
			cin >> t;
			stack.push_back(t);
		}
		else {
			if (order == "top") {
				if (stack.size() == 0) { cout << -1 << endl; }
				else { cout << stack.back() << endl;
				}
			}
			else if (order == "size") {
				cout << stack.size() << endl;

			}
			else if (order == "empty") {
				if (stack.size() == 0) { cout << 1 << endl; }
				else { cout << 0 << endl; }
				
			}
			else {
				if (stack.size() == 0) { cout << -1 << endl; }
				else { 
					t = stack.back();
					stack.pop_back();
					cout << t << endl; }

			}
		}
	}
}