#include<iostream>
using namespace std;
int main()
{
  int N,A[100],ce=0,co=0,i;
  cin>>N;
  for(i=0;i<N;i++)
  cin>>A[i];
  for(i=0;i<N;i++)
  {
     if(A[i]%2==0)
     ce++;
     else
     co++;
     }
     if(ce>co)
     cout<<"READY FOR BATTLE";
     else
     cout<<"NOT READY";
     return 0;
     }