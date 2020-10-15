/*************************************************************************
  > File Name: 8.c
  > Author: Crow
  > Mail: qnglsk@163.com 
  > Created Time: Thu Sep  3 15:41:11 2020
 ************************************************************************/

#include<stdio.h>

/*
 *  Use a copy function from Programming Exercise 2 to copy the third through fifth 
 *  elements of a seven-element array into a three-element array. The function itself need
 *  not be altered; just choose the right actual arguments. (The actual arguments need not 
 *  be an array name and array size. They only have to be the address of an array element 
 *  and a number of elements to be processed.) 
 */

/* one of the copy function in 2.c */

void ar_copy2(const double * ara, double * arb, int n);

int main(void)
{
	double ar[7] = { 1,2,3,4,5,6,7 };
	double ar2[4];
	ar_copy2(ar+2, ar2, 4);


	for (int i = 0; i < 4; i++)
		printf("%.0lf%c", ar2[i], " \n"[3==i]);

	return 0;
}

void ar_copy2(const double * ara, double * arb, int n)
{
	for (int i = 0; i < n; i++)
		*(arb++) = *(ara++);
}
