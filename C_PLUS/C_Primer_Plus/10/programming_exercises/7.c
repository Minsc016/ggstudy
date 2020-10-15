/*************************************************************************
  > File Name: 7.c
  > Author: Minsc
  > Mail: qnglsk@163.com 
  > Created Time: Thu Sep  3 11:47:40 2020
 ************************************************************************/

#include<stdio.h>

/*
 * Write a program that initializes a two-dimensional array-of- double and uses one of the 
 * copy functions from exercise 2 to copy it to a second two-dimensional array. (Because a
 * two-dimensional array is an array of arrays, a one-dimensional copy function can be used
 * with each subarray.) 
 * */

/* copy ar_copy2 func in 2.c to here */
void ar_copy2(const double * ara, double * arb, int n);

int main(void)
{
	double ar[4][3] = {
		{1,2,3},
		{4,5,6},
		{7,8,9},
		{10,11,12}
	};
	double ar2[4][3];
	for(int i = 0; i < 4; i++)
		ar_copy2(ar[i], ar2[i], 3);


	//
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 3; j++)
			printf("%.0lf%c", ar2[i][j], " \n"[j==2]);

	return 0;
}

void ar_copy2(const double * ara, double * arb, int n)
{
	for (int i = 0; i < n; i++)
		*(arb++) = *(ara++);
}
