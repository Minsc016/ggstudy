/*************************************************************************
	> File Name: 6.c
	> Author: Minsc
	> Mail: qnglsk@163.com 
	> Created Time: Thu Sep  3 11:02:26 2020
 ************************************************************************/

#include<stdio.h>

/*  Write a function that reverses the contents of an array of double and test it in a simple 
 *  program.
 *  */

void rev_ar(double ar[], int n);

int main(void)
{
	double arr[9] = { 1,3,5,7,9,8,6,4,2 };

	for(int i = 0; i < 9; i++)
		printf("\033[31;1m%.0lf%c\033[0m", arr[i], " \n"[8==i] );
	rev_ar(arr,9);
	for(int i = 0; i < 9; i++)
		printf("\033[31;1m%.0lf%c\033[0m", arr[i], " \n"[8==i] );


	return 0;
}

void rev_ar(double ar[], int n)
{
	double tmp;
	for (int i = 0; i < n / 2; i++)
	{
		tmp = ar[i];
		ar[i] = ar[n-i-1];
		ar[n-i-1] = tmp;
	}
}
