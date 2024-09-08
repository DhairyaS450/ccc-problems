import sys
data = sys.stdin.read().split('\n')

X = int(data[0])
same_groups = data[1:X + 1]

Y = int(data[X + 1])
diff_groups = data[X + 2: X + Y + 2]

G = int(data[X + Y + 2])
actual_groups = data[X + Y + 3: X + Y + G + 3]

names_pair_set = set([])

for t in actual_groups:
    name1, name2, name3 = t.split(" ")
    names_pair_set.add(f"{name1} {name2}")
    names_pair_set.add(f"{name1} {name3}")
    names_pair_set.add(f"{name2} {name1}")
    names_pair_set.add(f"{name2} {name3}")
    names_pair_set.add(f"{name3} {name1}")
    names_pair_set.add(f"{name3} {name2}")
    
total_violated = 0
for t in same_groups:
    if t not in names_pair_set:
        total_violated = total_violated + 1
for t in diff_groups:
    if t in names_pair_set:
        total_violated = total_violated + 1
print(total_violated)