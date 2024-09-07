def dusa_final_size(starting_size, yobi_sizes):
    dusa_size = starting_size
    for yobi in yobi_sizes:
        if yobi < dusa_size:
            dusa_size += yobi
        else:
            return dusa_size
    return dusa_size

# Reading input
import sys
input = sys.stdin.read
data = input().split()

starting_size = int(data[0])
yobi_sizes = list(map(int, data[1:]))

# Finding the final size
final_size = dusa_final_size(starting_size, yobi_sizes)
print(final_size)