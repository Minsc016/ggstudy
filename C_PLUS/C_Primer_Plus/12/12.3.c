/*************************************************************************
	> File Name: 12.3.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Fri Sep  4 11:26:25 2020
 ************************************************************************/

#include<stdio.h>

/* loc_stat.c -- using a local static variable */

void trystat(void);

int main(void)
{
	int count;

	for (count = 1; count <= 3; count++)
	{
		printf("Here comes iteration %d:\n", count);
		trystat();
	}

	return 0;
}

void trystat(void)
{
	int fade = 1;
	static int stay = 1;

	printf("fade = %d and stay = %d\n", fade++, stay++);
}
