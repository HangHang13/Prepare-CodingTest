import sys

input = sys.stdin.readline


n,m = map(int, input().split())


dict = {}

for i in range(1,n+1):
    a = input().rstrip()

    dict[i]=a
    dict[a]=i

print(dict)
# {1: 'Bulbasaur', 'Bulbasaur': 1, 2: 'Ivysaur', 'Ivysaur': 2, 3: 'Venusaur', 'Venusaur': 3, 4: 'Charmander',
#  'Charmander': 4, 5: 'Charmeleon', 'Charmeleon': 5, 6: 'Charizard', 'Charizard': 6, 7: 'Squirtle',
#  'Squirtle': 7, 8: 'Wartortle', 'Wartortle': 8, 9: 'Blastoise', 'Blastoise': 9, 10: 'Caterpie', 'Caterpie': 10, 11: 'Metapod', 'Metapod': 11, 12: 'Butterfree', 'Butterfree': 12, 13: 'Weedle', 'Weedle': 13, 14: 'Kakuna', 'Kakuna': 14, 15: 'Beedrill', 'Beedrill': 15, 16: 'Pidgey', 'Pidgey': 16, 17: 'Pidgeotto', 'Pidgeotto': 17, 18: 'Pidgeot', 'Pidgeot': 18, 19: 'Rattata', 'Rattata': 19, 20: 'Raticate', 'Raticate': 20, 21: 'Spearow', 'Spearow': 21, 22: 'Fearow', 'Fearow': 22, 23: 'Ekans', 'Ekans': 23, 24: 'Arbok', 'Arbok': 24, 25: 'Pikachu', 'Pikachu': 25, 26: 'Raichu', 'Raichu': 26}
for i in range(m):
    a = input().rstrip()
    if a.isdigit():
        print(dict[int(a)])
    else:
        print(dict[a])