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

bool isSquare(long x)
{
     long s = (long)sqrt(x);
     if (s*s == x)
          return true;
     return false;
}

int solve()
{
     int guess = 3;
     int SIZE = 100000;
     int primes[SIZE];
     int p = 3;
     for (int i = 0; i < SIZE; i++)
     {
          while (!isPrime(p))
               p += 2;
          primes[i] = p;
          p += 2;
     }
     // Brute force search of odd composite numbers
     while(1)
     {
          if (isPrime(guess))
          {
               guess += 2;
               continue;
          }
          int i = 0;
          for (i = 0; i < SIZE; i++)
          {
               int test =  ((guess-primes[i])/2);
               if (isSquare(test))
               {
                    break;
               }
          }
          if (i == SIZE)
          {
               cout << guess << endl;
               return guess;
          }
          guess += 2;
     }
}

int main()
{
     solve();
     return 0;
}
