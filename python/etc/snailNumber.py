
num = int(input())
#우 하 좌 상
dy = [0,1,0,-1]
dx = [1,0,-1,0]
lst = [[0]*num for _ in range(num)]
y,x = 0,0
idx=0
for a in range(1, num*num+1):
    lst[y][x] = a
    y += dy[idx]
    x += dx[idx]

    if x <0 or y < 0 or x>= num or y>=num or lst[y][x] != 0:
        y-=dy[idx]
        x-=dx[idx]

        idx = (idx+1)%4

        y+=dy[idx]
        x+=dx[idx]

# for x in lst:
#     for b in x :
#         print(b, end=" ")
#     print()
print(*lst)