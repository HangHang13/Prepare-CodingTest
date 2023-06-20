n = int(input())

words = list(input())

cnt = 0
for i in range(1, n):
    compareword = words[:]
    c, d = 0, 0
    word = list(input())
    for wor in word:
        if wor in compareword:
            compareword.remove(wor)
        else:
            c+=1
    if len(compareword) <2 and c<2:
        cnt+=1
print(cnt)