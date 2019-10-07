#include<iostream>
using namespace std;
int main()
{  long int T;
    
   cin>>T;
   for(int i=0;i<T;i++)
   { string a;
     cin>>a;
	int c=0;
     for(int j=0;j<7;j++)
     {
	if(a[j]!=a[j+1])
	c++;
	}
	if(a[7]!=a[0])
	c++;
	 if(c<=2)
	 cout<<"uniform"<<"\n";
	 else
	 cout<<"non-uniform"<<"\n";
	 
   }
   
   return 0;
}