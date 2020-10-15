/*************************************************************************
	> File Name: 13.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Thu Sep  3 17:28:21 2020
 ************************************************************************/

#include<stdio.h>

/*
 * Write a program that prompts the user to enter three sets of five double numbers each. 
 * (You may assume the user responds correctly and doesn’t enter non-numeric data.) The 
 * program should accomplish all of the following: 
 * a.  Store the information in a 3×5 array. 
 * b.  Compute the average of each set of five values. 
 * c.  Compute the average of all the values. 
 * d.  Determine the largest value of the 15 values. 
 * e.  Report the results. 
 * Each major task should be handled by a separate function using the traditional C 
 * approach to handling arrays. Accomplish task “b” by using a function that computes 
 * and returns the average of a one-dimensional array; use a loop to call this function three 
 * times. The other tasks should take the entire array as an argument, and the functions 
 * performing tasks “c” and “d” should return the answer to the calling program.
 * */

double ave_set(const double ar[], int n);
double ave_all(const double ar[][5], int n);
double lar(const double ar[][5], int n);

int main(void)
{
	double prom[3][5] = {
		{1,3,5,7,9},
		{4,5,6,7,8},
		{7,7,7,7,7}
	};

	for (int i = 0;i < 3;i++)
		printf("average of set%d:%.1lf\n", (i+1), ave_set(prom[i],5));

	printf("\naverate of all:%.1lf\n", ave_all(prom,3));
	printf("\nThe largest value of all:%.1lf\n",lar(prom,3));

	return 0;
}

double ave_set(const double ar[], int n)
{
	double sum=0;
	for(int i = 0; i < n; i++)
		sum += ar[i];

	return sum/n;
}

double ave_all(const double ar[][5], int n)
{
	double sum;
	const double *p = ar[0];
	for(int i = 0; i < n*5; i++, p++)
		sum += *p;

	return sum/(n*5);
}
double lar(const double ar[][5], int n)
{
	double larg_v = ar[0][0];
	for(int i = 0; i < n; i++)
		for(int j = 0; j < 5; j++)
			if(*(*(ar+i)+j) > larg_v)
				larg_v = *(*(ar+i)+j);
	
	return larg_v;
}
