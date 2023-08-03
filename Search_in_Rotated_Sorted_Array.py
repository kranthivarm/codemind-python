n=int(input())
l=list(map(int,input().split()))
piv=int(input())
ind=-1
for i in range(n):
    if l[i]==piv:
        ind=i
        break;
print(ind)