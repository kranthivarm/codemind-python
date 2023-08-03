n=int(input())
l=list(map(int,input().split()))
d={};cnt=0
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
        print(i)