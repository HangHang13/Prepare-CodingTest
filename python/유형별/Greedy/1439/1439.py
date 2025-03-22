

a = input()



cnt=0
index = 'a'

for i in a:
    if i != index:
        index= i
        cnt+=1

print(cnt//2)




