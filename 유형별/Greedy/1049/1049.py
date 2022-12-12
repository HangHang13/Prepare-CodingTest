n,m = map(int,input().split())


lst = []

for i in range(m):
    a,b = map(int,input().split())
    lst.append([a,b])
con= 0
_min=9999999
kim=0
_minTax = min(lst, key=lambda x:x[0])
# print(type(_minTax))
# print(_minTax[0])
_minPay = min(lst, key=lambda x:x[1])
# print(_minPay[1])



sixkim = int(n//6)
zero = int(n%6)


_min = min(_min, _minTax[0]*sixkim+_minPay[1]*zero, _minPay[1]*n, _minTax[0]*(sixkim+1) )

# _min = min(_min, _minTax[0], _minPay[1]*n)

print(_min)