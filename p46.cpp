#include <iostream>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

using namespace std;
typedef signed long long int int64;

bool isPerfectSquare(int64 n)
{
     if (n < 0)
          return false;
     int64 test = (int64)(sqrt(n)+0.5);
     return test*test == n;
}
/*
Input: n > 3, an odd integer to be tested for primality;
Input: k, a parameter that determines the accuracy of the test
Output: composite if n is composite, otherwise probably prime
write n . 1 as 2sddddddd with d odd by factoring powers of 2 from n . 1
LOOP: repeat k times:
   pick a random integer a in the range [2, n . 2]
   x . ad mod n
   if x = 1 or x = n . 1 then do next LOOP
   for r = 1 .. s . 1
      x . x2 mod n
      if x = 1 then return composite
      if x = n . 1 then do next LOOP
   return composite
return probably prime
*/

bool isPrime(long n)
{
     if (n == 2)
          return true;
     if (n < 3 || n % 2 == 0)
          return false;
     float lim = sqrt(n);

     for (int i = 3; i <= lim; i += 2)
     {
          if (n % i == 0)
               return false;
     }
     return true;

}

bool issPrime(long n)
{
     if (n == 2)
          return true;
     if (n < 3)
          return false;
     int k = 20;
     unsigned long s;
     unsigned long d = n-1;
     while (d % 2 == 0)
     {
          s++;
          d /= 2;
     }
     for (int i = 0; i < k; i++)
     {

          unsigned long a = rand() % (n-2);
          if (a < 2)
               a = 2;
          unsigned long x = (unsigned long)((unsigned long)pow(a,d) % n);
          if (x == 1 || x == n-1)
               continue;
          for (unsigned long r = 1; r < s; r++)
          {
               x = (x*x) % n;
               if (x == 1)
                    return false;
               if (x == n-1)
                    goto LOOP;
          }
          return false;
     LOOP:
          3;
     }
     return true;

}
int solve()
{
     int i = 9;
     bool found = false;
     int SIZE = 1000;
     unsigned long primes[SIZE];
     int k = 1;
     primes[0]=2;
     unsigned long p = 3;
     while (k < SIZE)
     {
          while (!isPrime(p))
               p += 2;
          primes[k] = p;
          k++;
     }

     while(!found)
     {
          if (isPrime(i))
          { 
               i += 2;
               continue;
          }

          k = 0;
          while (!isPerfectSquare((i-primes[k])/2) && (i-primes[k]) > 0)
          {
               if (k == SIZE)
               {
                    found = true;
                    return i;
               }
               k++;
          }

          i += 2;
     }
}

int main()
{
     int i = solve();
     cout << i << endl;
     return 0;
}
