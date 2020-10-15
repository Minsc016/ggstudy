/*************************************************************************
  > File Name: 13.c
  > Author: Crow
  > Mail: qnglsk@163.com 
  > Created Time: Thu Sep  3 17:28:21 2020
 ************************************************************************/

#include<stdio.h>

/*
   Do Programming Exercise 13, but use variable-length array function parameters.
*/
double ave_set(int n, const double ar[]);
double ave_all(int rs, int cs, const double ar[][cs]);
double lar(int rs, int cs, const double ar[][cs]);

int main(void)
{
	double prom[3][5] = {
		{1,3,5,7,9},
		{4,5,6,7,8},
		{7,7,7,7,7}
	};

	for (int i = 0;i < 3;i++)
		printf("average of set%d:%.1lf\n", (i+1), ave_set(5,prom[i]));

	printf("\naverate of all:%.1lf\n", ave_all(3, 5, prom));
	printf("\nThe largest value of all:%.1lf\n",lar(3, 5, prom));

	return 0;
}

double ave_set(int n, const double ar[])
{
	double sum=0;
	for(int i = 0; i < n; i++)
		sum += ar[i];

	return sum/n;
}

double ave_all(int rs, int cs, const double ar[][cs])
{
	double sum;
	const double *p = ar[0];
	for(int i = 0; i < rs*cs; i++, p++)
		sum += *p;

	return sum/(rs*cs);
}

double lar(int rs, int cs, const double ar[][cs])
{
	double larg_v = ar[0][0];
	for(int i = 0; i < rs; i++)
		for(int j = 0; j < cs; j++)
			if(*(*(ar+i)+j) > larg_v)
				larg_v = *(*(ar+i)+j);

	return larg_v;
}
