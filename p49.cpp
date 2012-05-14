#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

using namespace std;

bool isPrime(long x)
{
     if (x == 2)
          return true;
     if (x < 3 || x % 2 == 0)
          return false;
     float lim = sqrt(x);
     for (int i = 3; i <= lim; i += 2)
          if (x % i == 0)
               return false;
     return true;
}

int compare(const void *a, const void *b)
{
     return (*(int*)a - *(int*)b);
}

bool isPerm(int base, int other)
{
     int b[4];
     int o[4];
     for (int i = 0; i < 4; i++)
     {
          b[i] = base % 10;
          o[i] = other % 10;
          base /= 10;
          other /= 10;
     }
     qsort(b,4,sizeof(int),compare);
     qsort(o,4,sizeof(int),compare);
     for (int i = 0; i < 4; i++)
     {
          if (b[i] != o[i])
               return false;
     }
     return true;
}

int solve()
{
     for (int a = 1000; a <= 9999; a++)
     {
          for (int d = 1; d <= 9999; d++)
          {
               if (isPrime(a) && isPrime(a+d)
                   && isPrime(a+2*d) && isPerm(a,a+d)
                   && isPerm(a,a+2*d))
               {
                    cout << a << a+d << a+2*d << endl;
               }
          }
     }
     return 0;
}

int main()
{
     solve();
     return 0;
}
