/*************************************************************************
	> File Name: t.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Tue Sep  1 14:45:05 2020
 ************************************************************************/

#include<stdio.h>

int main(void)
{
	int * pt;
	int ** p2;
	int ar1[2][3] = { {0,0,0},{0,0,0} };
	int ar2[3][2] = { {1,2}, {3,4},{5,6} };

	pt = ar1[0];
	printf("pt:[%p]\n", pt);
	p2 = &pt;
	*p2 = ar2[0];

	printf("pt:[%p]\n", pt);
	printf("ar2[0]:[%p]\tp2:[%p]\t*p2[%p]\n", ar2[0], p2, *p2);
	printf("ar1[0][0]:[%d]\tar2[0][0]:[%d]\n", ar1[0][0], ar2[0][0]);

	return 0;
}

