# ðSWEA2105 ëì í¸ ê°ê²

## ðºíìí ê°ë

- ë¸ííì


## ðºíì´ê³¼ì 

- ë§ììì ìê°í´ ë´ëê² ê°ì¥ ì´ë ¤ì ë¤.
- ì¸ë±ì±ì¼ë¡ í ì§, ìë¡ì´ ë¦¬ì¤í¸ë¥¼ ë§ë¤ì´ì 1:1ëì ìí¬ì§ ê³ ë¯¼íë¤.
- tmpë¡ maxê°ì êµ¬íê³  ë¤ì tmpë¥¼ ì´ê¸°íìì¼ì£¼ê¸°

## ðºì½ë

```python
#ì¼ì´ì¤ìë ¥
num = int(input())

for tc in range(1,num+1):
    # N = len(Aj) M = len(Bj)
    N,M = map(int,input().split())
    
    #ì«ìë¦¬ì¤í¸
    Aj = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    
    #Ajê° í­ì ê¸¸ì´ê° ììê°ì¼ë¡ ë§ë¤ì´ì£¼ê¸° 
    if len(Aj) > len(Bj):
        Bj, Aj = Aj, Bj
        N, M = M, N
 
    #ì´ê¸°ê°
    cnt=0
    _max=0
    
    #ë§ììì
    for i in range(M-N+1):
        tmp = 0

        for j in range(N):
            tmp+=Aj[j]*Bj[j+i]
        
        #ìµëê° ì°¾ê¸°
        if tmp>_max:
            _max=tmp
    #ì¶ë ¥
    print(f'#{tc} {_max}')
```

