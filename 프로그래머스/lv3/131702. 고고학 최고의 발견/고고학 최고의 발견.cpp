#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> clockHands) {
    int answer = 100000000;
    for (int firstRotate = 0; firstRotate < 4; firstRotate++) {
        int t = firstRotate;
        vector<vector<int>> clock = clockHands;
        for (int n = 0; n < clockHands.size(); n++) {
            if (firstRotate & (1 << n)) {
                for (int i = 0; i < clockHands.size(); i++) {
                    clock[i][n] = (clock[i][n] + 3) % 4;
                }
            }
        }
        for (int i = 1; i < clockHands.size(); i++) {
            for (int j = 0; j < clockHands.size(); j++) {
                if (clock[i - 1][j] != 3) {
                    t += 4 - clock[i - 1][j];
                    for (int k = 0; k < clockHands.size(); k++) {
                        clock[k][j] = (clock[k][j] + 4 - clock[i - 1][j]) % 4;
                    }
                }
            }
        }
        if (clock.back().back() == 0) {
            answer = min(answer, t);
        }
    }
    return answer;
}