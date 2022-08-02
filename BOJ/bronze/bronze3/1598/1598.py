


# arr=[[0]*b for _ in range(4)]
#
#
# for n in range(0,b):
#     arr[0][n] = 1+4*n
#     arr[1][n] = 2+4*n
#     arr[2][n] = 3+4*n
#     arr[3][n] = 4+4*n
#
#
#
# k=[]
# for y in range(4):
#     for x in range(len(arr[0])):
#         if arr[y][x] == a or arr[y][x]==b:
#             k.append((y,x))
# # print(k)
#
# bb=abs(k[0][0]-k[1][0])+abs(k[0][1]-k[1][1])
#
# print(bb)

a,b = map(int, input().split())
x1 = (a-1)//4 + 1
y1 = (a-1)%4
x2 = (b-1)//4 + 1
y2 = (b-1)%4
print(abs(x2-x1) + abs(y2-y1))