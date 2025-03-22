

lst = input()

str = ""
idx= 0
while idx<len(lst):
    if lst[idx:idx+4] == "XXXX":
        str+="AAAA"
        idx+=4
    elif lst[idx:idx+2] == "XX":
        str+="BB"
        idx+=2
    elif lst[idx] == "X":
        str = -1
        break
    elif lst[idx] == ".":
        idx+=1
        str+="."




print(str)
