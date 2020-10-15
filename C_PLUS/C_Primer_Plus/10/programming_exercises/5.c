/*************************************************************************
	> File Name: 5.c
	> Author: Minsc
	> Mail: qnglsk@163.com 
	> Created Time: Thu Sep  3 10:54:23 2020
 ************************************************************************/

#include<stdio.h>

/*Write a function that returns the difference between the largest and smallest elements of 
 * an array-of- double . Test the function in a simple program. 
 * */

double lsdiff(const double ar[], int n);

int main(void)
{

	printf("the difference between the largest and smallest elements of array::%.1lf\n", \
			lsdiff((double []){ 1,3,5,7,9,8,6,4,2,0 }, 10));

	return 0;
}

double lsdiff(const double ar[],int n)
{
	int i,lv,sv;
	for( i = 1, lv = ar[0], sv = ar[0]; i < n; i++)
	{
		if( ar[i] < sv )
			sv = ar[i];
		if (ar[i] > lv)
			lv = ar[i];
	}
	return lv - sv;
}
