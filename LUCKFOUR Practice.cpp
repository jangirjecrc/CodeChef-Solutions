#include<iostream> 
using namespace std; 
void digit (int); 
 
int main() 
{ 
      int t,i,n;
      cin>>t;
      for(i=0;i<t;i++)
      {
            cin>>n;
            digit(n);
      }
      return 0;
      
}
void digit(int a) 
{ 
      int fours=0;
      while(a>0) 
      { 
            if(a%10==4)
            {
                  fours++;
            }
            a/=10;
            
      } 
      cout<<fours<<endl;
 
} 
