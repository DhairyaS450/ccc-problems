#include <iostream>
#include <vector>

int main() {
    int M, N, K;
    std::cin >> M >> N >> K;

    // Count the number of times each row and column has been brushed
    std::vector<int> rows_brush_count(M, 0);
    std::vector<int> cols_brush_count(N, 0);

    // Read the brushing instructions and update the counts
    for (int i = 0; i < K; i++) {
        std::string instruction;
        int num;
        std::cin >> instruction >> num;
        num -= 1; // Convert to 0-based index
        if (instruction == "R") {
            rows_brush_count[num]++;
        } else if (instruction == "C") {
            cols_brush_count[num]++;
        }
    }

    int total_gold = 0;
    // Check each cell and see how many times it has been brushed
    for (int row : rows_brush_count) {
        for (int col : cols_brush_count) {
            // The total number of times a cell has been brushed is the number of times the row has been brushed plus the number of times the column has been brushed
            // If a cell has been brushed an even number of times, it is black otherwise it is gold
            if ((row + col) % 2 == 1) {
                total_gold++;
            }
        }
    }

    std::cout << total_gold << std::endl;
    return 0;
}