#include<iostream>
using namespace std;
int main()
{
int T,i;
cin>>T;
for(i=0;i<T;i++)
{
int X,Y,Z;
cin>>X>>Y>>Z;

if(((Y+Z)==X)||((X+Z)==Y)||((X+Y)==Z))
 cout<<endl<<"yes";
else
cout<<endl<<"no";
}
return 0;
}