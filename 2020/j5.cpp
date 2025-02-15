#include <iostream>
#include <vector>
#include <deque>
#include <set>
#include <utility>

using namespace std;

// Read input
int M, N;
vector<vector<int>> grid;

void readInput() {
    cin >> M >> N;
    grid.resize(M, vector<int>(N));
    for (int i = 0; i < M; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> grid[i][j];
        }
    }
}

// Cache for factor pairs
vector<pair<int, int>> factor_cache[1001];

vector<pair<int, int>> get_factor_pairs(int num) {
    if (!factor_cache[num].empty()) {
        return factor_cache[num];
    }
    
    vector<pair<int, int>> factors;
    for (int i = 1; i * i <= num; ++i) {
        if (num % i == 0) {
            int x = i, y = num / i;
            if (x <= M && y <= N) {
                factors.emplace_back(x, y);
            }
            if (x != y && y <= M && x <= N) {
                factors.emplace_back(y, x);
            }
        }
    }
    factor_cache[num] = factors;
    return factors;
}

string bfs() {
    deque<pair<int, int>> queue;
    queue.emplace_back(1, 1); // Start from top-left
    set<pair<int, int>> visited;
    visited.emplace(1, 1); // Track visited cells

    while (!queue.empty()) {
        auto [x, y] = queue.front();
        queue.pop_front();

        // If we reached the bottom-right, return "yes"
        if (x == M && y == N) {
            return "yes";
        }
        
        int num = grid[x - 1][y - 1]; // Convert to 0-based indexing
        for (const auto& [nx, ny] : get_factor_pairs(num)) {
            if (visited.find({nx, ny}) == visited.end()) {
                visited.emplace(nx, ny);
                queue.emplace_back(nx, ny);
            }
        }
    }

    return "no";
}

int main() {
    readInput();
    cout << bfs() << endl;
    return 0;
}

