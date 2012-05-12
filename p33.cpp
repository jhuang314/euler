#include <iostream>
#include <stdio.h>
#include <cmath>
#include <limits>


using namespace std;

bool deq(double a, double b, double epsilon)
{
     return fabs(a - b) <= ( (fabs(a) > fabs(b) ? fabs(b) : fabs(a)) * epsilon);
}


void solve()
{
     for(int num = 11; num < 100; num++)
     {
          for(int denom = 11; denom < 100; denom++)
          {
               double frac = 1.0* num/denom;
               int num1 = num/10*10;
               int num2 = num%10;
               int d1 = denom/10*10;
               int d2 = denom%10;
               if (abs(frac-1.0*num2/d2) < 0.0001)
               {
                    cout << frac << endl;
               }
          }
     }
}
int main(int argc, char **argv)
{
     solve();
     return 0;
}
