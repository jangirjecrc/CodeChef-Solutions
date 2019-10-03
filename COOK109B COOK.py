# cook your dish here
t=int(input())
for i in range(t):
    x=10000000
    n=list(map(int,input().split()))
    for j in range(n[0]):
        cp=list(map(int,input().split()))
        for k in range(n[1]):
            if cp[0]>n[2]+1:
                cp[0]=cp[0]-1
            elif cp[0]<n[2]-1:
                cp[0]=cp[0]+1
            else:
                cp[0]=n[2]
        if cp[0]>=n[3] and cp[0]<=n[4]:
            if x>cp[1]:
                x=cp[1]
    if x==10000000:
        print('-1')
    else:
        print(x)
            
        