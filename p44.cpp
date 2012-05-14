#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <math.h>
using namespace std;


long pent(long x)
{
     return x * (3*x-1)/2;
}

bool isPent(long x)
{
     if (x < 0)
          return false;
     long disc = 1 + 24 * x;
     if ((int)sqrt(disc) * (int)sqrt(disc) == disc && ((int)sqrt(disc)+1)%6 == 0)
          return true;
     return false;
}

int main()
{
     int size = 1000000000;
     long min = 99999999999999;
/*
  long pents[size];
  
  for (long i = 1; i < size; i++)
  {
  pents[i] = pent(i);
  }
*/
     
     for (long i = 1000; i < size; i++)
     {
          
          for (long j = i+1; j < size; j++)
          {
               long sum = pent(i)+pent(j);
               long diff = pent(j)-pent(i);
               
               if (diff > min)
                    goto SKIP;
               if (isPent(sum) && isPent(diff))
               {
                    if (diff < min)
                    {
                         min = diff;
                    }
               }
          }
     SKIP:
          3;
     }
     cout << min << endl;
     
     
     return 0;
}
