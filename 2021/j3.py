prev = ""
while True:
    line = input()
    if line == "99999":
        break
    a = int(line[0])
    b = int(line[1])
    if a + b == 0:
        print(f'{prev} {line[2:]}')
    elif (a + b) % 2 == 0:
        print(f'right {line[2:]}')
        prev = "right"
    else:
        print(f'left {line[2:]}')
        prev = "left"