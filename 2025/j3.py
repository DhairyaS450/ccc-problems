num_of_codes = int(input())
for i in range(num_of_codes):
    code = input()
    new_char = ""
    int_list = []
    previous_int = False
    for char in code:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            new_char += char
            previous_int = False
        elif char.isdigit():
            if previous_int:
                int_list[-1] += char
            else:
                int_list.append(char)
            previous_int = True
        elif char == '-':
            int_list.append(char)
            previous_int = True
        else:
            previous_int = False

    new_char += str(sum(list(map(int, int_list))))
    print(new_char)

# ABCDEFC-20