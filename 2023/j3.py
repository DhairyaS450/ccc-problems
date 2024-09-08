number_of_people = int(input())
days = [0,0,0,0,0]
for i in range(number_of_people):
    availability = input()
    for j in range(len(availability)):
        if availability[j] == "Y":
            days[j] = days[j] + 1

best_days = [i+1 for i, x in enumerate(days) if x == max(days)]
print(','.join(map(str, best_days)))