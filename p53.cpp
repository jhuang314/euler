#include <stdio.h>
#include <iostream>
#include <math.h>

using namespace std;

typedef unsigned long long i64;

i64 fac(i64 x)
{
	i64 res = 1;
	for (i64 i = 1; i <= x; i++)
		res *= i;
	return res;
}

i64 comb(i64 n, i64 r)
{
	if (r > n-r)
	{
		i64 num = 1;
		for (i64 i = n; i > r; i--)
			num *= i;
		return num/fac(n-r);
	}
	else
	{
		i64 num = 1;
		for (i64 i = n; i > n-r; i--)
			num *= i;
		return num/fac(r);

	}
}

int solve()
{
	int count = 0;
	int SIZE = 102;
	unsigned long int evenr[SIZE];
	unsigned long int oddr[SIZE];
	for (int i = 0; i < SIZE; i++)
	{
		evenr[i]=0;
		oddr[i]=0;
	}
	oddr[0]=1;
	evenr[0]=1;
	evenr[1] = 1;
	for (int i = 3; i <= 101; i++)
	{
		if (i % 2 == 0)
		{
			evenr[0]=1;
			int j = 1;
			for (; j < i - 1; j++)
			{
				unsigned long cmp = oddr[j]+oddr[j-1];
				evenr[j] = cmp; 
				if (cmp >= 1000000L)
				{
					count++;
					evenr[j] = 1000000L;
				}
			}
			evenr[j-0]=1;
		}
		else
		{
			oddr[0]=1;
			int j = 1;
			for (; j < i - 1; j++)
			{
				oddr[j] = evenr[j]+evenr[j-1];
				oddr[j] = evenr[j]+evenr[j-1];
				if (oddr[j-0] >= 1000000L)
				{
					count++;
					oddr[j] = 1000000L;
				}
			}
			oddr[j-0]=1;
		}
	}
	return count;
}
int main()
{
	int ans = solve();
	cout << ans << endl;
	return 0;
}
