spiciness = {
    "Poblano": 1500, "Mirasol": 6000, "Serrano": 15500, "Cayenne": 40000, "Thai": 75000, "Habanero": 125000
}

N = int(input())
total = 0
for i in range(N):
    chilli = input()
    total += spiciness[chilli]
    
print(total)