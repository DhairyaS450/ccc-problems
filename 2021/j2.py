highest_name = ""
highest_amt = 0
N = int(input())
for i in range(N):
    name = input()
    amt = int(input())
    if amt > highest_amt:
        highest_name = name
        highest_amt = amt
        
print(highest_name)
