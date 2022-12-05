import sys
# input = sys.stdin.readline

while 1:
    a= input()

    if a == ".":
        break
    kk = []
    team=1
    for i in a:
        if i == "(" or i == "[":
            kk.append(i)
        elif i == "]":
            if kk and kk[-1]=="[":
                kk.pop()
            else:
                team =0
                break
        elif i == ")":
            if kk and  kk[-1] == "(":
                kk.pop()
            else:
                team =0
                break

    if team==1 and len(kk)==0:
        print("yes")
    else:
        print("no")