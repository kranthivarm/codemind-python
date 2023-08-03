n=int(input())
l=list(map(int,input().split()))
rot=int(input())
for i in range(rot):
    l.insert(0,l.pop(n-1))
print(*l)