no = set(range(1,10000))

noo = set()
for i in range(1,10001):
    for j in str(i):
        i += int(j)
    noo.add(i)

new = sorted(no-noo)
for j in new:
    print(j)