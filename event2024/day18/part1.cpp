#include <iostream>
#include <fstream>
#include <vector>
#include <cassert>
#include <queue>
#include <utility>

using namespace std;

int main(int argc, char** argv) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string line;
    ifstream fin(argv[1]);
    assert (fin);

    vector<string> matrix;

    while (getline(fin, line)) {
        matrix.push_back(line);
    }

    int n = matrix.size();
    int m = matrix[0].size();

    cout << "n = " << n << endl;
    cout << "m = " << m << endl;

    vector<vector<int>> D(n, vector<int>(m, 0));

    queue<pair<int, int>> q;
    q.push(make_pair(1, 0));

    int dr[4] = {0, 0, 1, -1};
    int dc[4] = {1, -1, 0, 0};

    while (!q.empty()) {
        auto [ci, cj] = q.front();
        q.pop();

        for (int k = 0; k < 4; k++) {
            int r = ci + dr[k];
            int c = cj + dc[k];

        }
    }

    return 0;
}
