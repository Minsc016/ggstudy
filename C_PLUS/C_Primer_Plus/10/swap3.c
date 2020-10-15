/*************************************************************************
	> File Name: swap3.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Mon Aug 31 11:25:50 2020
 ************************************************************************/

#include<stdio.h>

/* swap3.c -- using pointers to make swapping work */
void interchange(int * u, int * v);

int main(void)
{
	int x = 5, y = 10;
	printf("Originally x = %d and y = %d.\n", x, y);
	interchange(&x, &y); //sed addresses to function
	printf("Now x = %d and y = %d.\n", x, y);

	return 0;
}

void interchange(int * u, int * v)
{
	int temp;

	temp = *u;
	*u = *v;
	*v = temp;
}

