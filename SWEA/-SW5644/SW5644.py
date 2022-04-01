import sys
from collections import deque
sys.stdin = open('input.txt')


dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]
num = int(input())

for tc in range(1,num+1):
    # M 이동시간 A 충전소 갯수
    m,a = map(int,input().split())
    #a_list A 이동정보 b_list B 이동정보
    a_list = list(map(int,input().split()))
    b_list = list(map(int,input().split()))

    #배열
    arr= [[[(0, 0)] for _ in range(10)] for _ in range(10)]

    for case in range(a):
        y, x, c, p = map(int, input().split()) # (x, y)에 충전범위, 성능
        x, y = x - 1, y - 1
        for i in range(10):
            for j in range(10):
                if abs(i - x) + abs(j - y) <= c:
                    if arr[i][j] == 0:
                        arr[i][j] = [case + 1, p]
                    else:
                        arr[i][j].append((case + 1, p))

    ay, ax = 0, 0
    acac = [arr[ay][ax]]
    #a궤적
    for i in range(m):
        ay=ay+dy[a_list[i]]
        ax=ax+dx[a_list[i]]
        acac.append(arr[ax][ay])

    by,bx=9,9
    bcbc=[arr[by][bx]]
   #b궤적
    for i in range(m):
        by=by+dy[b_list[i]]
        bx=bx+dx[b_list[i]]
        bcbc.append(arr[bx][by])

    result = 0

    #print(acac)
    for i in range(m + 1):
        afinal = acac[i]
        bfinal = bcbc[i]
        afinal.sort(key=lambda x: -x[1])
        bfinal.sort(key=lambda x: -x[1])


        if len(afinal) == len(bfinal) == 1:
                continue

        if afinal[0][0] == bfinal[0][0]:
            result += afinal[0][1]
            result += max(afinal[1][1], bfinal[1][1])
        else:
            result += afinal[0][1] + bfinal[0][1]

    print(f'#{tc} {result}')



# # 10 * 10크기의 그래프, 사용자는 2명, (0,0) (9,9)에서 시작함.
#
# dx = [0, -1, 0, 1, 0]
# dy = [0, 0, 1, 0, -1]
#
# T = int(input())
# for tc in range(1):
#     n, a = map(int, input().split())
#     move_a = list(map(int, input().split()))
#     move_b = list(map(int, input().split()))
#     graph = [[[(0, 0)] for _ in range(10)] for _ in range(10)]
#
#     for case in range(a):
#         y, x, c, p = map(int, input().split()) # (x, y)에 충전범위, 성능
#         x, y = x - 1, y - 1
#         for i in range(10):
#             for j in range(10):
#                 if abs(i - x) + abs(j - y) <= c:
#                     if graph[i][j] == 0:
#                         graph[i][j] = [case + 1, p]
#                     else:
#                         graph[i][j].append((case + 1, p))
#     ax, ay = 0, 0
#     result_a = [graph[ax][ay]]
#     for i in range(n):
#         ax = ax + dx[move_a[i]]
#         ay = ay + dy[move_a[i]]
#         result_a.append(graph[ax][ay])
#
#     bx, by = 9, 9
#     result_b = [graph[bx][by]]
#     for i in range(n):
#         bx = bx + dx[move_b[i]]
#         by = by + dy[move_b[i]]
#         result_b.append(graph[bx][by])
#
#     result = 0
#     for i in range(n + 1):
#         cura = result_a[i]
#         curb = result_b[i]
#         cura.sort(key = lambda x: -x[1])
#         curb.sort(key = lambda x: -x[1])
#
#         if len(cura) == len(curb) == 1:
#             continue
#
#         if cura[0][0] == curb[0][0]:
#             result += cura[0][1]
#             result += max(cura[1][1], curb[1][1])
#         else:
#             result += cura[0][1] + curb[0][1]
#     for i in graph:
#         for x in i:
#             print(x, end="        ")
#         print()
#     print("#%d %d" %(tc, result))
