s1=input()
s2=input()
x1=[];x2=[]
for i in range(len(s1)):
    if s1[i]!='#':
        x1.append(s1[i])
    else:
        x1.pop()
for i in range(len(s2)):
    if s2[i]!='#':
        x2.append(s2[i])
    else:
        x2.pop()
if len(x1)==len(x2):
    for i in range(len(x2)):
        if x1[i]!=x2[i]:
            print("False")
            break
    else:
        print("True")
else:
    print("False")