import sys
input = sys.stdin.readline


arr = [list(map(int, input().split())) for _ in range(5)]



num = list(map(int, input().split()))

for _ in range(4):
    num += list(map(int,input().split()))


def check():
    #가로체크
    bingo=0
    for i in arr:
        if i.count(0)== 5:
             bingo+=1

    #세로체크

    for x in range(5):
        t=0
        for y in range(5):
            if arr[y][x] ==0:
                t+=1
        if t==5:
            bingo+=1

    #대각체크 좌
    d1=0
    for y in range(5):
        if arr[y][y] == 0:
            d1+=1
    if d1==5:
        bingo+=1
    d2=0

    for y in range(5):
        if arr[y][4-y] == 0:
            d2+=1
    if d2==5:
        bingo+=1

    return bingo
cnt=0
for i in range(25):
    for y in range(5):
        for x in range(5):
            if num[i] == arr[y][x]:
                arr[y][x] = 0
                cnt+=1
    if cnt>=12:
        res = check()
        if res>=3:
            print(i+1)
            break


