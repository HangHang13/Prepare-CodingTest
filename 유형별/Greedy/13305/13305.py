k=int(input())
road = list(map(int, input().split()))

fuel = list(map(int, input().split()))

fuel.pop()
# print(fuel)
# print(road)
_m=fuel[0]
_mf = fuel[0]*road[0]
for i in range(1,len(fuel)):
    if fuel[i] < _m:
        _m = fuel[i]

    _mf += _m*road[i]


print(_mf)