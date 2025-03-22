import sys
sys.stdin = open('sample_input.txt')

#swea에서 본 답
def check(film):
    for c in range(W):
        temp = ''
        success = False
        for r in range(D):
            temp = temp + str(film[r][c])

        for i in range(D - K + 1):
            sample = temp[i:i + K]
            if sample == '0' * K or sample == '1' * K:
                success = True
                break

        if not success:
            return False
    return True


def dfs(m, M, idx):
    if m == M:
        return check(film)

    for d in range(idx, D):
        for t in range(2):
            origin = film[d][:]
            film[d] = medicine[t][:]
            if dfs(m + 1, M, d + 1):
                return True
            film[d] = origin[:]


for tc in range(1, int(input()) + 1):
    D, W, K = map(int, input().split())
    film = []
    for _ in range(D):
        film.append(list(map(int, input().split())))

    medicine = [[0] * W, [1] * W]

    for M in range(D + 1):
        if dfs(0, M, 0):
            print(f'#{tc} {M}')
            break
