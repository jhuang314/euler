#include <stdio.h>
#include <iostream>
#include <math.h>
using namespace std;

bool isPan(long x, int n)
{
     unsigned int d[n+2];
     int len = (int)log10(x)+1;
     if (len != n)
          return false;
     for (int i = 1; i <= n; i++)
          d[i]=0;
     for (int i = 1; i <= n; i++)
     {
          int index = x % 10;
          if (d[index] != 0)
               return false;
          d[index]++;
          x /= 10;
     }
     return true;
     
}

int main()
{
     int list[] = {1,2,3,4,5,6,7,8,9};
     long max = 0;
     long pan = 0;
     for (long t = 1; t <= 100000; t++)
     {
          int len = (int)log10(t)+1;
          pan = 0;
          int i = 0;
          while ((unsigned)log10(pan)<8)
          {
               int lenlist = (int)log10(list[i]*t)+1;
               for (int k = 0; k < lenlist; k++)
                    pan *= 10;
               pan += list[i++] * t;
          }

          if ((int)log10(pan) == 8 && isPan(pan,9) && max < pan)
               max = pan;
     }
     cout << max << endl;
     return 0;
}
