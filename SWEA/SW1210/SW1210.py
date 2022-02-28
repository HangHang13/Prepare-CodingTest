import sys
sys.stdin = open('input.txt')


# dy = [0,0,-1]
# dx = [-1,1,0]
#
# for tc in range(10):
#     num = int(sys.stdin.readline())
#     lst = []
#     for a in range(100):
#         lst.append(list(map(int, input().split())))
#     fin = lst[-1].index(2)
#     print(fin)
#     y,x = 99, fin
#     while True:
#         if y==0:
#             print(f'#{num} {x}')
#             break
#         else:
#             for k in range(3):
#                 ny = y+dy[k]
#                 print(ny)
#                 nx = x+dx[k]
#                 print(nx)
#                 if 0<=ny<100 and 0<=nx<100 and lst[ny][nx] == 1:
#                     lst[ny][nx] == 0
#                     y,x = ny, nx
#                     break

# dy = [0, 0, -1]
# dx = [1, -1, 0]
dy = [0,0,-1]
dx = [-1,1,0]
for case in range(10):
    cs = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))

    y, x = 99, arr[-1].index(2)
    while True:
        if y == 0:
            print(f'#{cs} {x}')
            break
        else:
            for k in range(3):
                new_y = y + dy[k]
                new_x = x + dx[k]


                if 0 <= new_y < 100 and 0 <= new_x < 100 and arr[new_y][new_x] == 1:
                    arr[new_y][new_x] = 0
                    x, y = new_x, new_y
                    #break




# for t in range(1, 11):
#     T = int(input())
#     arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]
#     for i in range(102):
#         if arr[99][i] == 2:
#             h = i
#     up = [-1, 0, 0]
#     lr = [0, -1, 1]
#     v = 99
#     while v > 0:
#         for i in range(0, 3):
#             if arr[v+up[i]][h+lr[i]] == 1:
#                 arr[v][h] = 0
#                 v += up[i]
#                 h += lr[i]
#     print(f'#{t} {h-1}')

# def find_ladder_sol(board):
#     i = len(board) - 1
#     j = board[i].index(2)
#
#     while True:
#         i -= 1
#         if 0 <= j - 1 < 100 and board[i][j - 1] == 1:
#             while 0 <= j - 1 < 100 and board[i][j - 1] == 1:
#                 j -= 1
#             continue
#
#         if 0 <= j + 1 < 100 and board[i][j + 1] == 1:
#             while 0 <= j + 1 < 100 and board[i][j + 1] == 1:
#                 j += 1
#             continue
#
#         if i == 0:
#             return j
#
#
# for tc in range(1, 11):
#     n = int(input())
#     board = [list(map(int, input().split())) for _ in range(100)]
#
#     print(f'#{tc} {find_ladder_sol(board)}')