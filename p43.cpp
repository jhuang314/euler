#include <stdio.h>
#include <iostream>
#include <math.h>
using namespace std;

bool isPan(long x, int n)
{
     unsigned int d[n+2];
     int len = (int)log10(x)+1;
     if (len != n+1)
          return false;
     for (int i = 0; i <= n; i++)
          d[i]=0;
     for (int i = 0; i <= n; i++)
     {
          int index = x % 10;
          if (d[index] != 0)
               return false;
          d[index]++;
          x /= 10;
     }
     return true;
     
}

bool satisfy(long x)
{
     long test = x % 1000;
     int divis[] = {17,13,11,7,5,3,2};

     for (int i = 0; i < 7; i++)
     {
          if (test % divis[i] != 0)
               return false;
          x /= 10;
          test = x % 1000;
     }
     return true;
}

int main()
{
     int list[] = {1,2,3,4,5,6,7,8,9};
     long sum = 0;

     for (long t = 123456789; t <= 9876543210; t++)
     {
          if (satisfy(t) && isPan(t,9))
          {
               sum += t;
          }
     }
     cout << sum << endl;
     return 0;
}
