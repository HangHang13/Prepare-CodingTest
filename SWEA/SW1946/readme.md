# ๐SWEA1946

## ๐บํ์ํ ๊ฐ๋

- ์คํ?

- ์ฌ๋ผ์ด์ฑ

## ๐บํ์ด๊ณผ์ 

- ๋ฆฌ์คํธ์ ์ผ๋ ฌ๋ก ๋ํด์ ์ ์ฅํ ํ, ๊ทธ ๋ฆฌ์คํธ๋ฅผ 10์ฉ ์ธ๋ฑ์ฑ ์ถ๋ ฅ

## ๐บ์ฝ๋

```python
#์ผ์ด์ค ์๋ ฅ
num = int(input())

#์ผ์ด์ค ์คํ
for tc in range(1,num+1):
    
    #์ํ๋ฒณ ์
    case = int(input())

   
    lst1= []
    
    #์ํ๋ฒณ ์ ๋งํผ ๋ฐ๋ณต
    for _ in range(case):
        
        #์ํ๋ฒณ๊ณผ ์ซ์์๋ ฅ
        Alpha, num = input().split(" ")
        n= int(num)
        
        #๋ฆฌ์คํธ์ ์ผ๋ ฌ๋ก ์ ์ฅ
        
        lst1 = lst1 + list(Alpha*n)
        
		#์ถ๋ ฅ
    print(f'#{tc}')
    for k in range(len(lst1)//10+1):
        for a in lst1[10 * k:10 * (k + 1)]:
            print(a, end="")
        print()
        
        '''
        #1
        AAAAAAAAAA
        BBBBBBBCCC
        CC
        
        
        '''


```

