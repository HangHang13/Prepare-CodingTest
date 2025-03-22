

n,w,l = map(int, input().split())
trucks = list(map(int, input().split()))

weight=0
cnt=0
bridge = [0] * w

while 1:
    out = bridge.pop(0)
    weight -=out

    if trucks:
        if trucks[0]+weight <= l:
            bridge.append(trucks[0])
            weight += trucks[0]
            trucks.pop(0)
        else:
            bridge.append(0)

    cnt+=1

    if not bridge:
        break

print(cnt)