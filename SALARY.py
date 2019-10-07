t=int(input())

for i in range(t):
    
	n=int(input())
    
	a=list(map(int,input().split()))
    
	flag=1
   
	c=0
    
	mi=min(a)
    
	for j in range(n):
        
		c=c+a[j]-mi
    
	print(c)