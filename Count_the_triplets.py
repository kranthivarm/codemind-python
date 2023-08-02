for k in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    cnt=0
    for i in range(n):
        for j in range(i+1,n):
            if l[i]+l[j] in l:
                cnt+=1
    if cnt>0:
        print(cnt)                
    else :
        print(-1)