# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    max2=0
    max1=0
    for j in range(n):
        max2=(20*a[j])-(10*b[j])
        if max2>max1:
            max1=max2
    print(max1)
    
