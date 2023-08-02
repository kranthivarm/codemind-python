n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
x=0
cnt=0
k=0
if -1 in l1 and -1 in l2:
    print("Infinite")
else:
    if -1 in l1:
        for i in range(n):
            if l1[i]==-1:
                x=i
                break
        while sum(l1)<sum(l2):
            l1[i]=k
            k+=1
        if sum(l1)==sum(l2):
            cnt+=1
    elif -1 in l2:
        for i in range(l2):
            if l2[i]==-1:
                x=i
                break
        while sum(l2)<sum(l1):
            l2[i]=k
            k+=1
        if sum(l1)==sum(l2):
            cnt+=1
    print(cnt)