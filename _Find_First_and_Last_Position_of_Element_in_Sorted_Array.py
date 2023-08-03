n=int(input())
l=list(map(int,input().split()))
tar=int(input())
st=-1;en=-1
x=0
for i in range(n):
    if x==0 and l[i]==tar:
        st=i;
        en=i;
        x=1
    elif x==1 and l[i]==tar:
        en=i
print(st,en,end=" ")