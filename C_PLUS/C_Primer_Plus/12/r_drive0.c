/*************************************************************************
	> File Name: r_drive0.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Mon Sep  7 14:57:36 2020
 ************************************************************************/

#include<stdio.h>

/*test the rand0() function */
/* compile with rand0.c */

extern int rand0(void);

int main(void)
{
	int count;

	for (count = 0; count < 5; count++)
		printf("%d\n", rand0());

	return 0;
}
