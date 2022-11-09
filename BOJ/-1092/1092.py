n=int(input())

lst1 = list(map(int, input().split()))

m = int(input())

lst2 = list(map(int, input().split()))


lst1.sort(reverse=True)
lst2.sort(reverse=True)

print(lst2,lst1)