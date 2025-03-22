people = int(input())
cars = int(input())
capacity = int(input())

if people <= cars * capacity:
    print('yes')
else:
    print('no')