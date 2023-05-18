n=int(input())
ls=list(map(int,input().split()))
s=list(set(ls))
f=0
for i in s:
    if i%2!=0:
        f+=i
print(f)
