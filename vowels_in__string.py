s=input()
ls=[]
for i in s:
    if i=='a'or i=='e'or i=='i'or i=='o'or i=='u' or i=='A'or i=='E'or i=='I'or i=='O'or i=='U':
        if i not in ls:
            print(i,end=' ')
            ls.append(i)