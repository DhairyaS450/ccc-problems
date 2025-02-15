test = input()
line = input()

def get_cyclic_shifts(line):
    cyclic_shifts = []
    new_line = line + line
    for i in range(len(line)):
        cyclic_shifts.append(new_line[i:i+len(line)])
    return cyclic_shifts

cyclic_shifts = get_cyclic_shifts(line)

is_shift = False
for shift in cyclic_shifts:
    if shift in test:
        print("yes")
        is_shift = True
        break

if not is_shift:
    print("no")