#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
using namespace std;
bool isPalin(unsigned long long x)
{
	int len = log10(x);
	int num[len+2];
	for (int i = len; i >= 0; i--)
	{
		num[i] = x % 10;
		x /= 10;
	}
	int f=0;
	int b = len;
	while (f <= b)
	{
		if (num[f] != num[b])
			return false;
		f++;
		b--;
	}
	return true;
}

unsigned long long reverse(unsigned long long x)
{
	unsigned long long r = 0;
	while (x >= 1)
	{
		r *= 10;
		r += (x % 10);
		x /= 10;
	}
	return r;	
}
bool isLychrel(unsigned long long x)
{
	unsigned long long pal = x + reverse(x);
	for (int i = 0; i < 50; i++)
	{
		if (isPalin(pal))
		{
			return false;
		}
		pal += reverse(pal);
	}
	return true;
}
int solve()
{
	int count = 0;
	for (long i = 0; i < 10000; i++)
	{
		if (isLychrel(i))
			count++;
	}
	cout << count << endl;
	return count;
}

int main()
{
	solve();
	return 0;
}
