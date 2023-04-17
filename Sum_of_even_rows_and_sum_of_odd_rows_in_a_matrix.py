n,m=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
evsum=0;odsum=0
for i in range(n):
    for j in range(m):
        if i%2==0:
            evsum+=mat[i][j]
        else:
            odsum+=mat[i][j]
print(evsum,odsum)
