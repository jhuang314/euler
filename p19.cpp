#include <iostream>

using namespace std;

int month(int m,int y)
{
     switch(m)
     {
     case 1:
          return 3;
     case 2:
          if (y%4==0)
               return 1;
          else
               return 0;
     case 3:
          return 3;
     case 4:
          return 2;
     case 5:
          return 3;
     case 6:
          return 2;
     case 7:
          return 3;
     case 8:
          return 3;
     case 9:
          return 2;
     case 10:
          return 3;
     case 11:
          return 2;
     case 12:
          return 3;
     default:
          return -1;
     }
}

int solve()
{
     int d = 1;//day of week
     int m;//Jan
     int y;
     int count = 0;

     for(y=1900; y <= 2000; y++)
     {
          for (m = 1; m <= 12; m++)
          {
               d %= 7;
               if (d == 0 && y >= 1901)
                    count++;
               d += month(m,y);
          }
     }
     cout << "Num Sundays:" << count << endl;
     return count;

}

int main(int argc, char **argv)
{
     solve();
     return 0;
}
