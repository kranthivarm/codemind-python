a,b=0,0
for i in input():
    if i=='U':b+=1
    elif i=='D':b-=1
    elif i=='R':a+=1
    elif i=='L':a-=1
if a==0 and b==0:print("True")
else:print("False")