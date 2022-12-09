import sys
input = sys.stdin.readline

t=int(input())

def check(y):
    global cnt1, cnt0
    if y ==0:
        cnt0+=1
        return 0
    elif y==1:
        cnt1+=1
        return 1
    else:
        return check(y-2) + check(y-1)



for _ in range(t):
    c = int(input())
    zero, one = 1,0
    for i in range(c):
        zero,one = one , zero+one
    print(zero, one)






