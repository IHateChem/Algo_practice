#include <iostream>
#include <vector>
using namespace std;
int main() {
	int p, a;
	bool isasc = true;
	bool ismix = false;
	for (int i = 1; i < 9; i++) {
		cin >> a;
		if (isasc) {
			if (a == 9-i) {
				isasc = false;
			}
			else if (a != i) {
				ismix = true;
				break;
			}
		}
		else {
			if (a != 9 - i) {
			ismix = true;
			break;
		}

		}
	}
	if (ismix) {
		cout << "mixed";
	}
	else if (isasc) {
		cout << "ascending";
	}
	else {
		cout << "descending";
	}
	
}