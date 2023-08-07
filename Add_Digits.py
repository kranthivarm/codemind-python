n=int(input())
while n//10!=0:
    sum=0
    while n!=0:
        sum+=n%10
        n=n//10
    n=sum
print(n)