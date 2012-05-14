#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;
typedef unsigned long long bits;


int b(bits x)
{
	int count = 0;
	int len = (int)log10(x)+1;
	bits mul1 = 1;
	bits mul2 = 2;
	for (int i = 0; i <= len; i++)
	{
		if ((x & mul1) != 0 && (x & mul2) != 0)
		{
			count++;
		}
		mul1 <<= 1;
		mul2 <<= 1;
	}
	if (count % 2 == 0)
		return 1;
	return -1;
}

int g(bits t, bits c)
{
	bits sum = 0;
	bits counter = 0;
	bits i = 0;
	while(1)
	{
		sum += b(i);
		if (sum == t)
		{
			counter++;
			if (counter == c)
				return i;
		}
		i++;
	}
	return sum;
}

int main()
{

	cout << g(321,1) << endl;
	return 0;
}
