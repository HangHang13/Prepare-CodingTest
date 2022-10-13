a= int(input())
list1 = list(map(int, input().split()))
list1.sort()

list2=[]
cnt=0
for num in list1:
    cnt = cnt+num
    list2.append(cnt)

print(sum(list2))