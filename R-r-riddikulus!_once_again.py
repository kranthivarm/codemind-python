n,d=map(int,input().split())
l=list(map(int,input().split()))
for i in range(d):
    x=l[0]
    l.remove(x)
    l.append(x)
print(*l)