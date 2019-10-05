# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    if(n%2==0):
        print("-1")
    else:
        for j in range(n):
            c=arr.count(arr[j])
            if c==1:
                print(arr[j])
                break
    