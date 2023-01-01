#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;
class Node {
private:
	int value;
	Node* left;
	Node* right;
	bool _isleft = false;
	bool _isright = false;
public:
	int getvalue() {
		return value;
	};
	bool isleft() {
		return _isleft;
	};
	bool isright() {
		return _isright;
	};
	Node* getleft() {
		return left;
	};
	Node* getright() {
		return  right;
	};
	void setvalue(int a) {
		value = a;
	};
	void setleft(int a) {
		Node* N = new Node;
		N->setvalue(a);
		left = N;
		_isleft = true;
	};
	void setright(int a) {
		Node *N = new Node;
		N->setvalue(a);
		right = N;
		_isright = true;
	};
	void nodeprint() {
		if (_isleft) left->nodeprint();
		if (_isright) right->nodeprint();
		cout << value << endl;
	};
};
class Tree {
private:
	Node root;
	bool isNone = true;
public:
	bool isnone() {
		return isNone;
	};
	void insert(int a) {
		if (isNone) {
			root.setvalue(a);
			isNone = false;
		}else {
			Node *t = &root;
			while (1) {
				if (t->getvalue() > a) {
					if (t->isleft()) {
						t = t->getleft();
					}
					else break;
				}
				else {
					if (t->isright()) {
						t = t->getright();
					}
					else break;
				}
			}
			if (t->getvalue() > a) {
				t->setleft(a);
			}
			else {
				t->setright(a);
			}

		}
	};
	void printNode() {
		root.nodeprint();
	}
};
int main() {
	Tree T;
	int a;
	while (std::cin >> a) {
		T.insert(a);
	}
	T.printNode();
}