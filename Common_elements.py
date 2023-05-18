n,m=map(int,input().split())
ls1=list(map(int,input().split()))
ls2=list(map(int,input().split()))
lis1=[];lis2=[]
for i in ls1:
    if i not in lis1:
        lis1.append(i)
for i in ls2:
    if i not in lis2:
        lis2.append(i)
for i in lis1:
    if i in lis2:
        print(i,end=" ")
        