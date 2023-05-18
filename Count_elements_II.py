n,m=map(int,input().split())
ls1=list(map(int,input().split()))
ls2=list(map(int,input().split()))
se1=set(ls1)
se2=set(ls2)
cnt=0
for i in se1:
    if i not in se2:
        cnt+=1
for i in se2:
    if i not in se1:
        cnt+=1
print(cnt)