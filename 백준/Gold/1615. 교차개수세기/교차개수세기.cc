#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

vector<pair<int, int>> t_arr;
vector<int> arr;
long long answer;

void merge(int s, int e) {
    int m = (s + e) / 2;
    int pnt1 = s, pnt2 = m + 1, pnt3 = 0;
    vector<int> temparr(e - s + 1);
    while (pnt1 <= m && pnt2 <= e) {
        if (arr[pnt1] <= arr[pnt2]) {
            temparr[pnt3++] = arr[pnt1++];
        }
        else {
            temparr[pnt3++] = arr[pnt2++];
            answer += m - pnt1 + 1;
        }
    }
    while (pnt1 <= m) {
        temparr[pnt3++] = arr[pnt1++];
    }
    while (pnt2 <= e) {
        temparr[pnt3++] = arr[pnt2++];
    }
    for (int i = 0; i < e - s + 1; i++) {
        arr[s + i] = temparr[i];
    }
}

void mergeSort(int s, int e) {
    if (s < e) {
        int m = (s + e) / 2;
        mergeSort(s, m);
        mergeSort(m + 1, e);
        merge(s, e);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N, M;
    cin >> N >> M;
    arr.resize(M);
    t_arr.resize(M);
    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        t_arr[i] = {a,b};
    }
    sort(t_arr.begin(), t_arr.end());
    int i = 0;
    for (pair<int, int> p : t_arr) {
        arr[i++] = p.second;
    }
    mergeSort(0, M - 1);
    cout << answer << '\n';
    return 0;
}
