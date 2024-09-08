c = int(input())

row1 = []
row2 = []

# init row 1
s = input()
row1 = s.split()

# init row 2
s = input()
row2 = s.split()

total = 0

'''
Rules:
each black tile requires 3 meters of tape
but if the right side is black, we save 2 meters
but if the down side is black, we save 2 meters

The upper row takes care of the up-down neighbours (lower row doesn't need to check its upper neighbour again)
The left tile takes care of the left-right neighbours (right tile doesn't need to check its left neighbour again)

'''

for i in range(c):

    if row1[i] == '1':
        total += 3

        # You need to check its right tile
        if i < c - 1 and row1[i+1] == '1':
            total -= 2

        '''
        5 columns
        index: 0 - 4
        last column index -> 4, which doesn't have right tile
        i < 5 - 1 =4 
        i < 4
        
        '''
        # You need to check its below tile
        if i % 2 == 0 and row2[i] == '1':
            total -= 2

    if row2[i] == '1':
        total += 3

        # You need to check its right tile
        if i < c - 1 and row2[i+1] == '1':
            total -= 2

print(total)