buger =[]
drink = []

for _ in range(3):
    buger.append(list(map(int, input().split())))

for _ in range(2):
    drink.append(list(map(int, input().split())))


aa=min(buger)
bb=min(drink)

cc= aa[0]+bb[0]-50

print(cc)