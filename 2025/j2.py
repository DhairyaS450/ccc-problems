available_donuts = int(input())
events = int(input())
for i in range(events):
    action = input() # + or -
    amount = int(input())

    if action == "+":
        available_donuts += amount
    elif action == '-':
        available_donuts -= amount

print(available_donuts)