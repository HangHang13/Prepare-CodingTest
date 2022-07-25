for _ in range(3):
    n = int(input())

    lst = []

    for _ in range(n):
        lst.append(int(input()))
    # print(lst)
    a = sum(lst)

    if a>0:
        print('+')
    elif a==0:
        print(0)
    else:
        print('-')
#
# i=0
# while i>3:
#     n = int(input())
#
#     lst = []
#
#     for _ in range(n):
#         lst.append(int(input()))
#     # print(lst)
#     a = sum(lst)
#
#     if a > 0:
#         print('+')
#     elif a == 0:
#         print(0)
#     else:
#         print('-')
#
#     i+=1
