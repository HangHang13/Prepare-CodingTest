import sys
sys.stdin = open('input.txt')


#스위치수
tc = int(sys.stdin.readline())
#스위치 리스트
#0 1 0 1 0 0 0 1
switch = [-1]+list(map(int, sys.stdin.readline().split()))
students = int(sys.stdin.readline())
def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return

for _ in range(students):
    gender, num = map(int, sys.stdin.readline().split())
    if gender ==1:
        for i in range(num, tc+1, num):
            change(i)
    else:
        change(num)
        for k in range(tc//2):
            if num+k>tc or num-k<1 : break
            if switch[num+k] == switch[num+k]:
                change(num-k)
                change(num+k)
            else:
                break

for i in range(1,tc+1):
    print(switch[i], end = " ")
    if i % 20 ==0:
        print()


#1 0 0 0 1 1 0 1



# elif gender == 2:
#     # num 기준으로 대칭인 아이들의 상태를 바꾸겠어
#     switch[num] = not switch[num]
#     k = 1
#     while 1:
#         if num - k >= 1 and num + k <= n:
#             if switch[num - k] == switch[num + k]:
#                 switch[num - k] = not switch[num - k]
#                 switch[num + k] = not switch[num + k]
#             else:
#                 break
#         else:
#             break
#         k += 1
#         print(switch, num,  k, "여자 while 안쪽")
#     print(switch, '여자 다음 스위치')


