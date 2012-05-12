#include <iostream>
#include <math.h>
#include <stack>

using namespace std;

bool isPrime(int x)
{
     if (x < 2)
          return false;
     if (x == 2)
          return true;
     if (x % 2 == 0)
          return false;
     for(int i = 3; i <= sqrt(x); i+=2)
          if (x%i==0)
               return false;
     return true;
}

bool trunc(int i)
{
     int t = i;
     stack<int> nums;
     int base = 0;
     if (!isPrime(i))
          return false;
     while (t > 9)
     {
          t /= 10;
          if (!isPrime(t))
               return false;
          base++;
          nums.push(t);
     }
     while (!nums.empty())
     {
          if (!isPrime(i-(int)pow(10,base)*nums.top()))
               return false;
          base--;
          nums.pop();
     }
     return true;
}

void solve()
{
     int count = 0;
     int sum = 0;
     int i = 10;
     while (count < 11)
     {
          while (!trunc(i))
               i++;
          sum += i;
          cout << i << endl;
          count++;
          i++;
     }
     cout << sum << endl;
}

int main(int argc, char **argv)
{
     solve();
     return 0;
}
