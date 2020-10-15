/*************************************************************************
	> File Name: arf.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Mon Aug 31 20:33:38 2020
 ************************************************************************/

#include<stdio.h>
#define SIZE 5
/* arf.c -- array functions */

void show_array(const double ar[], int n);
void mult_array(double ar[], int n,double mult);
int main(void)
{
	double dip[SIZE] = {20.0,17.66,8.2,15.3,22.22};

	printf("The original dip array:\n");
	show_array(dip,SIZE);
	mult_array(dip,SIZE,2.5);
	printf("The dip array after calling mult_array():\n");
	show_array(dip,SIZE);

	return 0;
}


/* display array contents */
void show_array(const double ar[], int n)
{
	/*
	for( int i = 0; i < n; i++ )
		printf("%8.3f ",ar[i]);
	putchar('\n');
	*/
	for(int i = 0; i< n; i++)
		printf("%8.3f%c",ar[i]," \n"[n-1==i]);
}

/* multiplies echo array member by the same multiplier */
void mult_array(double ar[], int n, double mult)
{
	for ( int i = 0; i < n; i++ )
		ar[i] *= mult;
}


