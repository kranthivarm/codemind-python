n=int(input())
ls=list(map(int,input().split()))
i=-1;j=0;
new=[]
for k in range(0,len(ls),2):
    new.append(ls[j])
    new.append(ls[i])
    j+=1;i-=1;
if len(ls)%2==1:
    new[-1]=0
for i in new:
    print(i,end=" ")