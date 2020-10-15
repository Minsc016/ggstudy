/*************************************************************************
	> File Name: day_mon3.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Mon Aug 31 14:59:12 2020
 ************************************************************************/

#include<stdio.h>

#define MONTHS 12
int main(void)
{
	int days[MONTHS] = { 31,28,31,30,31,30,31,31,30,31,30,31 };
	int index;

	for ( index = 0; index < MONTHS; index++ )
		printf("Month %2d has %d days,\n", index+1,
				*(days + index )); // same as days[index]

	return 0;
}
