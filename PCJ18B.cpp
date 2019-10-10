#include<iostream>
using namespace std;
int main()
{
   unsigned long int T,i;
   cin>>T;
   for(i=0;i<T;i++)
   {
     long long int n;
     cin>>n;
     unsigned long long int s=0;
     while(n>0)
     {
       s=s+(n*n);
       n=n-2;
     }
     cout<<endl<<s; }
   return 0;
}