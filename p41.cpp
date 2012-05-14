#include <stdio.h>
#include <iostream>
#include <math.h>
using namespace std;
bool isPrime(long x)
{
     if (x == 2)
          return true;
     if (x < 3 || x % 2 == 0)
          return false;
     float lim=sqrt(x);
     for (long i = 3; i <= lim; i += 2)
          if (x % i == 0)
               return false;
     return true;
}

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
