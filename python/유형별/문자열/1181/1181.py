n=int(input())

lsy=[]
for _ in range(n):
    lsy.append(input())
    # lsy.append(input())
lsy = set(lsy)
lsy=list(lsy)
lsy.sort()
lsy.sort(key=lambda x: len(x))

for a in lsy:
    print(a)