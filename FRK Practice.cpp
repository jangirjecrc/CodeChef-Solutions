#include<string.h>
#include<iostream>
using namespace std;
int main()
{                  
	int T,i,count=0,j,l;
	char a[3],b[30];
	cin>>T;
	for(i=0;i<T;i++)
      {	cin>>b;
	l=strlen(b);
	  for(j=0;j<(l-1);j++)
	  {

  if((b[j]=='c'&&b[j+1]=='h')||(b[j]=='h'&&b[j+1]=='e')||(b[j]=='e'&&b[j+1]=='f'))
	   { count++;
	   break;
	   }
	   }
	   }
	   cout<<count;

	return 0;
}