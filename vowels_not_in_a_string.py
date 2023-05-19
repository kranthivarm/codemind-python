s=input()
ls=[]
for i in s:
    if i=='a'or i=='e'or i=='i'or i=='o'or i=='u':
        ls.append(i)
temp=['a','e','i','o','u'];cnt=0
for i in temp:
    if i not in ls:
        cnt+=1
        print(i,end=' ')
if cnt==0:
    print(0)