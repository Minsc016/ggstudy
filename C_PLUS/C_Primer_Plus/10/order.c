/*************************************************************************
	> File Name: order.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Mon Aug 31 15:47:40 2020
 ************************************************************************/

#include<stdio.h>

/* order.c -- precedence in pointer operations */

int data[2] = {100,200};
int moredata[2] = {300,400};
int main(void)
{
	int * p1, * p2, * p3;

	p1 = p2 = data;
	p3 = moredata;
	printf("*p1 = %d,\t*p2 = %d,\t*p3 = %d\n", *p1, *p2 ,*p3);
	printf("*p1++ = %d,\t*p2++ = %d,\t(*p3)++ = %d\n", *p1++,*p2++,(*p3)++);
	printf("*p1 = %d,\t*p2 = %d,\t*p3 = %d\n", *p1, *p2, *p3);

	return 0;
}
