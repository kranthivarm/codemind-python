s=input()
l=len(s)
D=l;I=0
li=[]
for i in range(l):
    if s[i]=='I':
        li.append(I)
        I+=1
    elif s[i]=='D':
        li.append(D)
        D-=1
if s[l-1]=="I":
    li.append(I)
else:
    li.append(D)
print(*li)