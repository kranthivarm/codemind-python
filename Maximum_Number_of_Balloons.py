s=input()
balon=[0,0,0,0,0]
for i in s:
    if i=='b':balon[0]+=1
    elif i=='a':balon[1]+=1
    elif i=='l':balon[2]+=1
    elif i=='o':balon[3]+=1
    elif i=='n':balon[4]+=1
balon[2]//=2
balon[3]//=2
print(min(balon))