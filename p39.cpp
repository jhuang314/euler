#include <iostream>
#include <math.h>
#include <stdio.h>

using namespace std;

int solve()
{
     int max = 0;
     int maxp = 0;
     for(int p = 3; p <= 1000; p++)
     {
          int lima = (int)(p/(sqrt(2)+2)+1);
          int count = 0;
          for (int a = 1; a < lima; a++)
          {
               for (int b = 1; b <= p; b++)
               {
                    int c = p-a-b;
                    if (c > 0 && (a*a+b*b)==(c*c))
                    {
                         count++;
                    }
               }
          }
          if (count > max)
          {
               max = count;
               maxp = p;
          }
     }
     cout << maxp << endl;
     return maxp;
}
int main(int argc, char **argv)
{
     solve();
     return 0;
}
