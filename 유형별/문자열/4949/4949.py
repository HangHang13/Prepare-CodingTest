import sys
input = sys.stdin.readline

while 1:
    a= input()
    if a ==".":
        break
    kk = []

    for i in a:
        if i =="(" or i =="[":
            kk.append(i)
        elif i =="]":

