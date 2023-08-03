n=int(input())
if n<=2:
    print("The pattern is not possible")
else:
    for i in range(n):
        for j in range(i+1):
            print('*',end="")
        if i<n:
            print()
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            print('*',end="")
        if i>-1:
            print()