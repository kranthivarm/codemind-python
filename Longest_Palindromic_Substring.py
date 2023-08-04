s=input()
temp=""
ma=0
for i in range(len(s)):
    temp=""
    for j in range(i,len(s)):
        temp+=s[j]
        if temp==temp[::-1]:
            l=len(temp)
            if l>ma:
                ma=l
                res=temp
print(res)            