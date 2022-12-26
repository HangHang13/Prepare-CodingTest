n=int(input())


cnt=0

arr=[]
for _ in range(n):
    a=int(input())
    arr.append(a)



for i in range(n-2, -1, -1):
    if arr[i] >= arr[i+1]:
        cnt += arr[i] - arr[i+1] +1
        arr[i] = arr[i+1]-1

print(cnt)