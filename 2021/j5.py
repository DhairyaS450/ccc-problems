M = int(input())
N = int(input())
K = int(input())

#Count the number of times each row and column has been brushed
rows_brush_count = [0 for _ in range(M)]
cols_brush_count = [0 for _ in range(N)]

#Read the brushing instructions and update the counts
for i in range(K):
    instruction, num = input().split()
    num = int(num) - 1
    if instruction == "R":
        rows_brush_count[num] += 1
    elif instruction == "C":
        cols_brush_count[num] += 1

total_gold = 0
#Check each cell and see how many times it has been brushed
for row in rows_brush_count:
    for col in cols_brush_count:
        #The total number of times a cell has been brushed is the number of times the row has been brushed plus the number of times the column has been brushed
        #If a cell has been brushed an even number of times, it is black otherwise it is gold
        if (row + col) % 2 == 1:
            total_gold += 1

print(total_gold)