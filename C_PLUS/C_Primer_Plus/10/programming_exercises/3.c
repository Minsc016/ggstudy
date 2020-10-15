/*************************************************************************
	> File Name: 3.c
	> Author: Minsc
	> Mail: qnglsk@163.com 
	> Created Time: Thu Sep  3 10:07:54 2020
 ************************************************************************/

#include<stdio.h>
/*
 *  Write a function that returns the largest value stored in an array-of- int . Test the function 
 *  in a simple program. 
 *  */

int ar_max(int ar[], int n);

int main()
{
	printf("larges value in array:%d\n", \
			ar_max( (int []){ 1, 3, 5, 7, 9, 10, 8, 6, 4, 2 },10 ) );

	return 0;
}

int ar_max(int ar[], int n)
{
	int max_v,i;
	for (i = 1, max_v = ar[0]; i < n; i++)
		if (ar[i] > max_v)
			max_v = ar[i];

	return max_v;
}

