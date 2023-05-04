#include <iostream>
#include <list>
#include <unordered_map>
#include <vector>
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	unordered_map<int, pair<int, int>> station_map;
	int N, M, t;
	string order;
	cin >> N >> M;
	vector<int> stations;
	for (int i = 0; i < N; i++) {
		cin >> t;
		stations.push_back(t);
	}
	for (int i = 0; i < N; i++) {
		int p = (i == 0) ? N - 1 : i - 1;
		int n = (i == N - 1) ? 0 : i + 1;
		station_map[stations[i]]= make_pair(stations[p], stations[n]);
	}
	for (int i = 0; i < M; i++) {
		cin >> order;
		int a, b, t;
		int j = 0;
		cin >> a;
		if (order == "BN") {
			cin >> b;
			t = station_map[a].second;
			station_map[a].second = b;
			station_map[b] = make_pair(a, t);
			station_map[t].first = b;
		}
		else if (order == "BP") {
			cin >> b;
			t = station_map[a].first;
			station_map[a].first = b;
			station_map[b] = make_pair(t, a);
			station_map[t].second = b;

		}
		else if (order == "CP") {
			t = station_map[a].first;
			int tp = station_map[t].first;
			station_map[tp].second = a;
			station_map[a].first = tp;
            station_map.erase(t);
		}
		else if (order == "CN") {
			t = station_map[a].second;
			int tn = station_map[t].second;
			station_map[tn].first = a;
			station_map[a].second = tn;
            station_map.erase(t);
		}
		cout << t << '\n';
	}
}