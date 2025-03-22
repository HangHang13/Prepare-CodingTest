a=[]

for _ in range(5):
    b=int(input())
    if b<40:
        b=40
    a.append(b)

c=round(sum(a)/5)

print(c)