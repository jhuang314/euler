#include <iostream>
#include <stdio.h>
#include <math.h>
#include <inttypes.h>

using namespace std;

int solve(int x)
{
     long long digits = 0LL;
     unsigned long long term = 0LL;
     for(long unsigned int s = 1; s <= x; s++)
     {
          term = s;
          for(int i = 1; i < s; i++)
          {
               term *= s;
               term %= 10000000000LL;
          }
          digits += (term%10000000000LL);
          digits %= 10000000000LL;
          term = 0;
     }
     cout << digits << endl;
     return digits;
}

int main(int argc, char **argv)
{
     solve(1000);
     return 0;
}
