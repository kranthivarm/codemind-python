t=int(input())
for k in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    cnt=0
    for i in range(n):
        if i==0:
            cnt+=1
        else:
            if l[i]<=l[i-1]:
                cnt+=1
            else:
                l[i]=l[i-1]
    if i==n-1:
        print(cnt)
    else:
        print(cnt,end=" ")