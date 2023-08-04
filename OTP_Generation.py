res=""
for i in input():
    num=int(i)
    if num%2==1:
        res+=str(num*num)
print(res)