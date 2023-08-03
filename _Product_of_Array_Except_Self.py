n=int(input())
l=list(map(int,input().split()))
res=[]
for i in range(n):
    pro=1
    for j in range(n):
        if j==i:
            continue
        else:
            pro*=l[j]
    res.append(pro)
print(*res)