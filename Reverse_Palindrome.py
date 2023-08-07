x=int(input())
rev=str(x)
rev=rev[::-1]
x+=int(rev)
rev=str(x)
rev=rev[::-1]
while x!=int(rev):
    rev=str(x)
    rev=rev[::-1]
    x+=int(rev)
    rev=str(x)
    rev=rev[::-1]
print(x)