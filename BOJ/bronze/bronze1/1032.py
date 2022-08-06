import sys
input = sys.stdin.readline

t = int(input())

lst = list(input())

for _ in range(t-1):
    b= list(input())

    for a in range(len(lst)):
        if lst[a]!=b[a]:
            lst[a]='?'
        else:
            continue

print(''.join(lst))