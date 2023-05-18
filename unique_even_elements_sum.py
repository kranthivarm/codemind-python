n=int(input())
ls=list(map(int,input().split()))
se=set(ls)
summ=0
for i in se:
    if i%2==0:
        summ+=i
print(summ)
     