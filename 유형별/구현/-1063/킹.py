a, b, n = input().split()

n = int(n)
# 좌우상하오른위대각왼쪽위대각
move_info = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, -1, -1, 1, 1]

y, x = 8 - int(a[1]), ord(a[0]) - ord('A')
sy, sx = 8 - int(b[1]), ord(a[0]) - ord('A')

for _ in range(n):
    cmd = move_info.index(input())
    king_ny, king_nx = y + dy[cmd], x + dx[cmd]

    if 0 <= king_nx < 8 and 0 <= king_ny < 8:
        if king_ny == sy and king_nx == sx:
            stone_ny, stone_nx = sy + dy[cmd], sx + dx[cmd]
            if 0 <= stone_ny < 8 and 0 <= stone_nx < 8:
                sy, sx = stone_ny, stone_nx
                y, x = king_ny, king_nx
        else:
            y, x = king_ny, king_nx

#
print(chr(x + ord('A')) + str(8-y))
print(chr(sx + ord('A')) + str(8-sy))
