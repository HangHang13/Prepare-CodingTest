n,m = map(int, input().split())


ant1 = list(input())
ant2 = list(input())
t=int(input())
ant1.reverse()
ant3 = ant1 + ant2

for _ in range(t):
    for i in range(len(ant3)-1):
        if ant3[i] in ant1 and ant3[i+1] in ant2:
            ant3[i], ant3[i+1] = ant3[i+1], ant3[i]
            if ant3[i+1] == ant1[-1]:
                break


print("".join((ant3)))