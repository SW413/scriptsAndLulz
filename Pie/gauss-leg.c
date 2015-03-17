#include <stdio.h>
#include <math.h>

double nextA(double a, double b)
{
	return (a + b)/2;
}

double nextB(double a, double b)
{
	return sqrt(a * b);
}

double nextT(double t, double p, double thisA, double nextA)
{
	return t - (p * (thisA - nextA) * (thisA - nextA));
}

double nextP(double p)
{
	return 2 * p;
}

double calculatePi(double a, double b, double t)
{
	double numPart, den;

	numPart = (a + b);
	den = 4 * t;

	return (numPart * numPart) / den;
}

double gaussLeg(int iterations)
{
	double a[iterations], b[iterations], t[iterations], p[iterations];
	int i;

	a[0] = 1;
	b[0] = 1/sqrt(2);
	t[0] = 0.25;
	p[0] = 1;

	for ( i = 1; i <= iterations; i++ )
	{
		int prev = i - 1;
		a[i] = nextA(a[prev], b[prev]);
		b[i] = nextB(a[prev], b[prev]);
		t[i] = nextT(t[prev], p[prev], a[prev], a[i]);
		p[i] = nextP(p[prev]);
	}

	return calculatePi(a[iterations], b[iterations], t[iterations]);
}

int main(int argc, char const *argv[])
{
	printf("%.20f\n", gaussLeg(3));

	return 0;
}
