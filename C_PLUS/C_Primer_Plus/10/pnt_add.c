/*************************************************************************
	> File Name: pnt_add.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Mon Aug 31 11:41:35 2020
 ************************************************************************/

#include<stdio.h>
#define SIZE 4

int main(void)
{
	short dates [ SIZE ];
	short * pti;
	short index;
	double bills[SIZE];
	double * ptf;

	pti = dates;	// assign address of array to pointer
	ptf = bills;
	printf("%23s %15s\n", "short", "double");
	for (index = 0; index < SIZE; index++)
		printf("pointers + %d: %10p\t%10p\n",
				index,pti + index, ptf + index);

	return 0;
}

