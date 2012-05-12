#include <iostream>
#include <stdio.h>
#include <cmath>
#include <limits>

using namespace std;

int gcd(long a, long b)
{
	if (a < b)
	{
		long temp = a;
		a = b;
		b = temp;
	}
	if (a % b == 0)
		return b;
	return gcd(b, a%b);
}

void reduce(int *frac)
{
	if (sizeof(frac)/sizeof(int) <= 1)
		return;
	int factor = gcd(frac[0],frac[1]);
	*frac++ /= factor;
	*frac /= factor;
}
bool deq(double a, double b, double epsilon)
{
	return fabs(a - b) <= ( (fabs(a) > fabs(b) ? fabs(b) : fabs(a)) * epsilon);
}

void solve()
{
	int n1,n2,d1,d2;
	int n[] = {1,1};
	int i = 0;
	for (n1 = 1; n1 <= 9; n1++)
	{
		for (n2 = 1; n2 <= 9; n2++)
		{
			for (d1 = 1; d1 <= 9; d1++)
			{
				for (d2 = 1; d2 <= 9; d2++)
				{
					if (1.0*(n1*10+n2)/(d1*10+d2) < 1 && d1==n2)
					{
						int raw[] = {n1*10+n2,d1*10+d2};
						reduce(raw);
						int cancel[] = {n1,d2};
						reduce(cancel);
						if (raw[0]==cancel[0] && raw[1]==cancel[1])
						{
							printf("%d%d/%d%d=%d/%d\n",n1,n2,d1,d2,raw[0],raw[1]);
							n[0] *= (n1*10+n2);
							n[1] *= (d1*10+d2);
						}
					}
				}
			}
		}
	}
	reduce(n);
	printf("%d/%d\n",n[0],n[1]);
}

int main(int argc, char **argv)
{
	solve();
	return 0;
}
