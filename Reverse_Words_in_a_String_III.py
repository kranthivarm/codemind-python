s=input()
x=s.split()
s1=''
for i in range(len(x)):
    x[i]=x[i][::-1]
    if i!=len(x)-1:
        s1=s1+x[i]+' '
    else :
        s1=s1+x[i]
print(s1)