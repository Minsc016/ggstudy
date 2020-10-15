/*************************************************************************
	> File Name: array_memadd.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Mon Aug 31 20:13:54 2020
 ************************************************************************/

#include<stdio.h>

void add_to(int ar[], int n, double val);

int main()
{
	int marbles[10] = { 20,10,5,39,4,16,19,26,31,20 };
	for( int i = 0;i < 10; i++ )
		printf("%d%c",marbles[i],i==9?'\n':',');
	add_to(marbles,10,1);

	for( int i = 0; i < 10; i++ )
		printf(",%d" + !i, marbles[i]);
	printf("\n");

	return 0;
}

void add_to(int ar[], int n, double val)
{
	int i;
	for( i = 0; i < n; i++)
		ar[i] += val;
}

