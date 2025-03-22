import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
x = int(input())
cnt=0
left = 0
right = n-1


while left != right:
    if lst[left] + lst[right] == x:
        cnt+=1
        left+=1
    elif lst[left] + lst[right] >x:
        right-=1
    else:
        left+=1
print(cnt)