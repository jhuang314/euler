#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>

using namespace std;

string binary( unsigned long n )
{
     char     result[ (sizeof( unsigned long ) * 8) + 1 ];
     unsigned index  = sizeof( unsigned long ) * 8;
     result[ index ] = '\0';

     do result[ --index ] = '0' + (n & 1);
     while (n >>= 1);

     return string( result + index );
}
string convertInt(int number)
{
     if (number == 0)
          return "0";
     string temp="";
     string returnvalue="";
     while (number>0)
     {
          temp+=number%10+48;
          number/=10;
     }
     for (int i=0;i<temp.length();i++)
          returnvalue+=temp[temp.length()-i-1];
     return returnvalue;
}

bool isPalindrome(string ps)
{
     int l = ps.length()-1;

     int i = 0;
     while (i <= l)
     {
          if(ps.c_str()[i]!=ps.c_str()[l])
               return false;
          i++; l--;
     }
     return true;
}
int solve()
{
     string d;
     string b;
     int count = 0;
     for(int i = 1; i < 1000000; i++)
     {
          d = convertInt(i);
          if (isPalindrome(d))
          {
               b = binary(i); 
               if (isPalindrome(b))
                    count += i;
          }
     }
     cout << count << endl;
     return count;
}

int main(int argc, char **argv)
{
     solve();
     return 0;
}
