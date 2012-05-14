#include <stdio.h>
#include <iostream>
#include <math.h>

using namespace std;

void swap(unsigned long long frac[])
{
	unsigned long long temp = frac[0];
	frac[0] = frac[1];
	frac[1] = temp;
}

int solve()
{
	unsigned long long frac[] = {1,2};
	unsigned long long sqrt2[] = {1,1};
	unsigned long count = 0;
	for (int i = 0; i < 999; i++)
	{
		frac[0] += (2 * frac[1]);
		swap(frac);
//		printf("%llu/%llu\n",frac[0]+frac[1],frac[1]);
		if ((int)log10(frac[0]+frac[1])-(int)log10(frac[1]) >= 1)
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
