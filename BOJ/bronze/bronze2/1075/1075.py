a=input()
b= int(input())

c=int(a[:-2]+'00')

while 1:
    if c % b ==0:
        break
    c+=1

print(str(c)[-2:])