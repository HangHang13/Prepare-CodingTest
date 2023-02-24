n,k =map(int,  input().split())


w = ["?"] * n
idx= 0
check = True
for i in range(k):
    s,alpha = input().split()
    idx = (idx + int(s)) % n
    if w[idx] == "?":
        w[idx] = alpha
    else:
        if w[idx] == alpha:
            continue
        check= False

if check:
    idx = w.index(alpha)
    for i in range(idx, -n+idx,-1):
        print(w[i], end="")
else:
    print("!")


