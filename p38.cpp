#include <stdio.h>
#include <iostream>
#include <math.h>
using namespace std;

bool isPan(long x, int n)
{
     unsigned int d[n+2];
     for (int i = 1; i <= n; i++)
          d[i]=0;
     int len = (int)log10(x)+1;
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
     long max = 0;
     for (long i = 987654321; i >= 0; i-=2)
     {
          if (isPan(i,(int)log10(i)+1))
          {
               if (isPrime(i))
               {
                    cout << i << endl;
                    return 0;
               }
          }
     }
     return 0;
}
