import sys
import collections
sys.stdin = open('sample_input.txt')

T = int(input())

dr, dc = [1, 1, -1, -1], [1, -1, -1, 1]


def dfs(r, c, d, cnt):
    global ans

    for i in range(2):
        tmp_d = (d + i) % 4
        rr, cc = r + dr[tmp_d], c + dc[tmp_d]
        if start_r <= rr < N and 0 <= cc < N:
            if cnt != 0 and rr == start_r and cc == start_c:
                ans = max(ans, cnt + 1)
                return
            if array[rr][cc] not in dessert:
                dessert.append(array[rr][cc])
                dfs(rr, cc, tmp_d, cnt + 1)
                dessert.pop()


for test_case in range(1, T + 1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for r in range(N - 1):
        for c in range(1, N - 1):
            dessert = [array[r][c]]
            start_r, start_c = r, c
            dfs(r, c, 0, 0)

    print(f'#{test_case} {ans if ans != 0 else -1}')
