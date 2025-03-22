a,b= input().split()



std1=''
std2=''
std3=''
std4=''
for i in range(len(a)):
    if a[i] == '5':
        std1 +='6'
    else:
        std1 += a[i]
for i in range(len(b)):
    if b[i] == '5':
        std2 += '6'
    else:
        std2 += b[i]
for i in range(len(a)):
    if a[i] == '6':
        std3 += '5'
    else:
        std3 += a[i]
for i in range(len(b)):
    if b[i] == '6':
        std4 += '5'
    else:
        std4 += b[i]

aa =int(std1)+int(std2)
bb =int(std3)+int(std4)

print(bb,aa)