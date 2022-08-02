a=[]

for _ in range(3):
    b=int(input())
    a.append(b)


if sum(a)==180:
    if a[0]==a[1]==a[2]:
        print('Equilateral')
    elif (a[0]==a[1] and a[0]!=a[2] and a[1]!=a[2]) or (a[1]==a[2] and a[1]!=a[0] and a[2]!=a[0]) or (a[0]==a[2] and a[0]!=a[1] and a[2]!=a[1]):
        print('Isosceles')
    else:
        print('Scalene')

else:
    print('Error')