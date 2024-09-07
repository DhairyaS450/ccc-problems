#include <iostream>
#include <vector>
using namespace std;

int n, m, ans = 0;
vector<string> grid;

void dfs(int x, int y) { 
    if (x < 0 || x >= n || y < 0 || y >= m || grid[x][y] == '*') return;
    if (grid[x][y] == 'S') ans+=1;
    else if (grid[x][y] == 'M') ans+=5;
    else if (grid[x][y] == 'L') ans+=10;
    grid[x][y] = '*';
    dfs(x + 1, y);
    dfs(x - 1, y);
    dfs(x, y + 1);
    dfs(x, y - 1);
}

int main() {
    cin >> n >> m;
    grid.resize(n);
    for (int i = 0; i < n; i++) cin >> grid[i];
    int x, y;
    cin >> x >> y;
    dfs(x, y);
    cout << ans << endl;
}