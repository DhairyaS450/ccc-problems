number_of_players = int(input())
players_gold = 0
all_gold = True
for i in range(number_of_players):
    points = int(input())
    fouls = int(input())
    rating = points * 5 - fouls * 3
    if rating > 40:
        players_gold += 1
    else:
        all_gold = False
        
if all_gold:
    print(f'{players_gold}+')
else:
    print(players_gold)