t=int(input())
for i in range(t):
    ab=list(map(int,input().split()))
    s=ab[0]+ab[1]
    c=0
    st=[6,2,5,5,4,5,6,3,7,6]
    while(s):
        t=s%10
        c=c+st[t]
        s=int(s/10)
    print(c)