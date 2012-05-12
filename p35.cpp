#include <iostream>
#include <math.h>

using namespace std;
bool isPrime(int x)
{
     if (x == 2)
          return true;
     if (x % 2 == 0)
          return false;
     for(int i = 3; i <= sqrt(x); i+=2)
          if (x%i==0)
               return false;
     return true;
}
bool rotate(int x)
{
     int size = (int)log10(x);
     int result = x;
     
     for (int i = 0; i <= size; i++)
     {
          int digit = result % 10;
          int rest = result / 10;
          result = digit*(int)pow(10,size);
          result += rest;
          if (!isPrime(result))
               return false;
     }
     return true;

}

int main(int argc, char **argv)
{
     int count = 1;
     for (int i = 3; i < 1000000; i += 2)
     {
          if (rotate(i))
          {
               count++;
          }
     }
     cout << count << endl;
     return 0;
}
