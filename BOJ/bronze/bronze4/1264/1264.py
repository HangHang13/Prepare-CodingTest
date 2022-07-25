import sys
sys.stdin = open('input.txt')


lst = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
k=[]
kk=[]
while 1:
    n=input()
    if n == '#':
        break
    k=[]
    for a in range(0,len(n)):
        k.append(n[a])

    cnt = 0
    for a in k:
        if a in lst:
            cnt += 1
        else:
            continue

    print(cnt)


