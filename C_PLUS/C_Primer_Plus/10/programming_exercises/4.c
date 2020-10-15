/*************************************************************************
	> File Name: 4.c
	> Author: Minsc
	> Mail: qnglsk@163.com 
	> Created Time: Thu Sep  3 10:29:20 2020
 ************************************************************************/

#include<stdio.h>
/*
 * Write a function that returns the index of the largest value stored in an array-of- double. 
 * Test the function in a simple program. 
 * */

int mav_ind(const double ar[], int n);

int main(void)
{
	printf( "the index of the largest value in array:%d\n", mav_ind( (double []){ 1.1,2.2,3.3,4.4,3.3,2.2,1.1 } ,7) );

	return 0;
}

int mav_ind(const double ar[], int n)
{
	int i,id;
	for( i = 0, id = i; i < n - 1; i++)
		if ( ar[i] < ar[i+1])
			id = i + 1;

	return id;
}
