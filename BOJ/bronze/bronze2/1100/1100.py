arr = [list(input()) for _ in range(8)]


cnt = 0

for y in range(8):
    for x in range(8):
        if y % 2 ==1 and x % 2 ==1 and arr[y][x] == 'F':
            cnt+=1
        if y% 2 == 0 and x% 2 ==0  and arr[y][x] =='F':
            cnt+=1
print(cnt)