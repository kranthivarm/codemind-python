for k in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    x=sorted(l)
    if x==l:
        print(0)
    else:
        print(max(l)-min(l))