s=input()
n=int(input())
cnt=0;i=0;res=0
l=len(s)
if n<=l:
    for i in range(0,n+1):
        if s[i]=='a':cnt+=1
    res=cnt
else:
    for i in s:
        if i=='a':cnt+=1
    res=(n//l)*cnt;
    cnt=0
    x=n%l
    for i in range(0,x):
        if s[i]=='a':cnt+=1
    res+=cnt;
print(res)