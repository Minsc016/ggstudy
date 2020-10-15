/*************************************************************************
	> File Name: const_pointer_c.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Tue Sep  1 15:31:29 2020
 ************************************************************************/

#include<stdio.h>

int main(void)
{
	const int y = 4;
	const int * p2 = &y;
	int * p1;


	int x = 6;
	const int * p3 = &x;
	int * p4;

	p1 = p2;

	printf("*p1:%d", *p1);
/*	*p1 = 8;				// 错误
	printf("*p1:%d", *p1); */

	p3 = p4;
	printf("*p3:%d",*p3);

	*p3 = 8;
	printf("*p3:%d",*p3);


	return 0;
}

