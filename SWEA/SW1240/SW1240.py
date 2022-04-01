import sys
sys.stdin = open('input.txt')


def check(lst):
    if ((lst[0]+lst[2]+lst[4]+lst[6])*3+lst[1]+lst[3]+lst[5]+lst[7]) % 10 ==0:
        return sum(lst)
    return 0

T= int(input())

for tc in range(1,T+1):
    #n세로, m가로
    n,m = map(int,input().split())
    pdict = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }

    list_2=[]
    password=list(input() for _ in range(n))

    for y in range(n):
        for x in range(m-1,-1,-1):
            if password[y][x] =='1':
                for a in range(x-55,x-5,7):
                    tmp = pdict.get(password[y][a:a+7])
                    list_2.append(tmp)
            if len(list_2)>0:
                break




    print(f'#{tc} {check(list_2)}')





