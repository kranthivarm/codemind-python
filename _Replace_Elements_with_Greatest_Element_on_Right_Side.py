n=int(input())
l=list(map(int,input().split()))
temp=l.copy()
res=[]
for i in range(n):
    if i==n-1:
        res.append(-1)
    else:
        temp.remove(l[i])
        res.append(max(temp))
print(*res)