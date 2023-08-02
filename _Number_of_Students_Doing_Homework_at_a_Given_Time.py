n=int(input())
l=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
q=int(input())
cnt=0
for i in range(min(n,m)):
    if l[i]<=q and l2[i]>=q:
        cnt+=1
print(cnt)        