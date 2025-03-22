import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 0
    result_cnt = 9999999999

    for i in range(100):
        if arr[0][i]==1:
            cnt=0
            y,x = 0,i
            while True:
                if x<99 and arr[y][x+1] == 1:
                    while x<99 and arr[y][x+1] == 1:
                        x+=1
                        cnt+=1
                    else:
                        y+=1
                elif x>0 and arr[y][x-1] ==1:
                    while x>0 and arr[y][x-1] ==1:
                        x-=1
                        cnt+=1
                    else:
                        y+=1
                elif arr[y+1][x] ==1:
                    y+=1

                if y==99:
                    if result_cnt>=cnt:
                        result_cnt=cnt
                        result = i
                    break

    print(f'#{tc} {result}')
# dy=[0,0,-1]
# dx=[1,-1,0]
# def check(x):
#     y=99
#     cnt=0
#     while y>0:
#         if y == 0:
#             print(f'#{num} x: {x} cnt : {cnt}')
#             break
#         else:
#             for k in range(3):
#                 ny = y + dy[k]
#                 nx = x + dx[k]
#                 if 0 <= nx < 100 and 0 <= ny < 100 and board[ny][nx] == 1:
#                     board[ny][nx] = 0
#                     cnt += 1
#                     y, x = ny, nx
#
#         y-=1
#
#     return cnt, x
#
# for _ in range(1):
#     num = int(input())
#     board = []
#
#     for a in range(100):
#         board.append(list(map(int, input().split())))
#     print(board[99][1])
#
#     start = []
#     for a in range(100):
#         if board[99][a] ==1:
#             start.append(a)
#
#     print(start)
#
#
#     for x in start:
#         print(check(x))

# def ladder(arr, i, j):
#     cnt = 0
#     while i > 0:
#         if j + 1 <= 99 and arr[i][j + 1] == '1':
#             while j + 1 <= 99 and arr[i][j + 1] == '1':
#                 j += 1
#                 cnt += 1
#         elif j - 1 >= 0 and arr[i][j - 1] == '1':
#             while j - 1 >= 0 and arr[i][j - 1] == '1':
#                 j -= 1
#                 cnt += 1
#         i -= 1
#         cnt += 1
#     return cnt, j


# for _ in range(10):
#     tc = int(input())
#     arr = [input().split() for _ in range(100)]
#     test = arr
#     start_ls = []
#     min_cnt = 10000
#     min_j = 0
#     for i in range(100):
#         if arr[99][i] == '1':
#             start_ls.append(i)
#     for s in start_ls:
#         cnt, j = ladder(arr, 99, s)
#         if cnt < min_cnt:
#             min_cnt = cnt
#             min_j = j
#     print(f'#{tc} {min_j}')


# for tc in range(1, 11):
#     t = int(input())
#     arr = [list(map(int, input().split())) for _ in range(100)]
#     result = 0
#     result_cnt = 9999999999
#     for i in range(100):
#         if arr[0][i] == 1:  # 첫번째 줄에서 1인애들 찾기, 찾으면
#             cnt = 0
#             x, y = i, 0  # x == i y == 0
#             while True:
#                 if x < 99 and arr[y][x + 1] == 1:  # 오른쪽으로가자
#                     while x < 99 and arr[y][x + 1] == 1:
#                         x += 1
#                         cnt += 1
#                     else:
#                         y += 1
#                 elif x > 0 and arr[y][x - 1] == 1:
#                     while x > 0 and arr[y][x - 1] == 1:
#                         x -= 1
#                         cnt += 1
#                     else:
#                         y += 1
#                 elif arr[y + 1][x] == 1:
#                     y += 1
#                 if y == 99:
#                     if result_cnt >= cnt:
#                         result_cnt = cnt
#                         result = i
#                     break
#
#     print(f'#{tc} {result}')