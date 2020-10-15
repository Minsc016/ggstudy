/*************************************************************************
  > File Name: 2.c
  > Author: Minsc
  > Mail: qnglsk@163.com 
  > Created Time: Thu Sep  3 09:04:28 2020
 ************************************************************************/

/*
 * Write a program that initializes an array-of- double and then copies the contents of the 
 * array into three other arrays. (All four arrays should be declared in the main program.) To 
 * make the first copy, use a function with array notation. To make the second copy, use a 
 * function with pointer notation and pointer incrementing. Have the first two functions 
 * take as arguments the name of the target array, the name of the source array, and the 
 * number of elements to be copied. Have the third function take as arguments the name 
 * of the target, the name of the source, and a pointer to the element following the last 
 * element of the source. That is, the function calls would look like this, given the following 
 * declarations: 
 * double source[5] = {1.1, 2.2, 3.3, 4.4, 5.5};
 * double target1[5];
 * double target2[5];
 * double target3[5];
 * copy_arr(target1, source, 5);
 * copy_ptr(target2, source, 5);
 * copy_ptrs(target3, source, source + 5); 
 * */
#include<stdio.h>

void ar_copy(const double ara[], double arb[], int n);
void ar_copy2(const double * ara, double * arb, int n);
void ar_copy3(const double ara[], double arb[], double * plast);
int main()
{
	double ar1[30] = {[0] = 1,[29]=1};
	double ar2[30];
	
	//ar_copy(ar1,ar2,30);
//	ar_copy2(ar1, ar2, 30);
	ar_copy3(ar1, ar2, ar1 + 30);

	for (int i = 0; i < 30; i++)
		printf("\033[31;1m%.0f=%.0f%c\033[0m", ar1[i], ar2[i], " \n"[0==(i+1)%10]);

	return 0;
}

void ar_copy(const double ara[], double arb[], int n)
{
	for (int i = 0; i < n; i++)
		arb[i] = ara[i];
}

void ar_copy2(const double * ara, double * arb, int n)
{
	for (int i = 0; i < n; i++)
		*(arb++) = *(ara++);
}

void ar_copy3(const double ara[], double arb[], double * plast)
{
	while (ara < plast)
		*(arb++) = *(ara++);
}
