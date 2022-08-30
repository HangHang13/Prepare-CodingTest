a= list(input())

start = 'A'
res=0
for i in a:
    left_word = ord(start) - ord(i)
    right_word = ord(i) - ord(start)

    if left_word < 0:
        left_word+=26
    elif right_word <0:
        right_word+=26

    res+=min(left_word,right_word)
    start = i
print(res)