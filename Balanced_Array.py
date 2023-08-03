for k in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    temp=[0]
    for i in range(n):
        if i==0:
            if sum(l)-l[i]==sum(temp):
                print("YES")
                break
            else:
                temp.append(l[i])
                l[i]=0
                continue
        elif i==n-1:
            lsum=sum(l)-l[i]
            rsum=sum(temp)
            if lsum==rsum:
                print("YES")
                break
            else:
                temp.append(l[i])
                l[i]=0
        else:
            lsum=sum(temp)
            rsum=sum(l)-l[i]
            if lsum==rsum:
                print("YES")
                break
            else:
                temp.append(l[i])
                l[i]=0
    else:
        print("NO")