#include <iostream>

using namespace std;

int factorial(int x)
{
     int accum = 1;
     for (int i = 1; i <=x; i++)
          accum *= i;
     return accum;
}

bool works(int x)
{
     int t = x;
     int digit;
     int accum = 0; 
     while(t >= 1)
     {
          digit = t%10;
          t /= 10;
          accum += factorial(digit);
     }
     if (accum == x)
          return true;
     else
          return false;
}
int main()
{
     int accum = 0;
     for (int i = 3; i < 10000000; i++)
          if (works(i))
               accum += i;
     cout << accum << endl;
     return 0;
}
